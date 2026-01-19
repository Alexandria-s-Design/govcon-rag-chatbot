// Vercel Serverless Function for GovCon Intelligence Chatbot
// Uses OpenRouter with DeepSeek R1 (FREE)

const SYSTEM_PROMPT = `You are GovCon Intelligence, an expert advisor on federal government contracting.

EXPERTISE AREAS:
- FAR (Federal Acquisition Regulation)
- DFARS and agency supplements
- Contract types and pricing strategies
- Small business programs (8(a), HUBZone, WOSB, SDVOSB)
- SAM.gov registration and compliance
- Proposal development and evaluation
- Past performance documentation
- GSA schedules and contract vehicles

STRICT GUIDELINES:
1. Only answer questions about government contracting
2. If asked about unrelated topics, politely redirect: "I specialize in government contracting. For questions about [topic], please consult an appropriate resource. Is there anything about federal procurement I can help you with?"
3. Never provide legal, tax, or financial advice - suggest consulting professionals
4. If uncertain, acknowledge limitations clearly
5. Always cite relevant FAR sections or regulations when applicable
6. Use plain language - explain jargon when used

FORMATTING RULES:
- Do not use markdown formatting (no **, no __, no #, no \`\`\`)
- Use plain text with clear paragraph breaks
- Use numbered lists (1. 2. 3.) or bullet points for lists
- Keep responses concise but thorough
- Structure longer answers with clear sections`;

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { question } = req.body;

    if (!question) {
      return res.status(400).json({ error: 'Question is required' });
    }

    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://charlesmartinedd.github.io/govcon-rag-chatbot/',
        'X-Title': 'GovCon Intelligence'
      },
      body: JSON.stringify({
        model: 'deepseek/deepseek-r1-0528:free',
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: question }
        ],
        temperature: 0.1,
        max_tokens: 4096
      })
    });

    if (!response.ok) {
      const errorData = await response.text();
      console.error('OpenRouter error:', errorData);
      return res.status(500).json({
        error: 'LLM request failed',
        fallback: true
      });
    }

    const data = await response.json();
    const answer = data.choices?.[0]?.message?.content || '';

    // Extract potential sources from the answer (FAR references)
    const sources = extractSources(answer);

    // Calculate confidence based on response quality
    const confidence = calculateConfidence(answer, question);

    return res.status(200).json({
      answer: cleanResponse(answer),
      sources: sources.length > 0 ? sources : ['FAR - acquisition.gov'],
      confidence
    });

  } catch (error) {
    console.error('Handler error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      fallback: true
    });
  }
}

// Extract FAR/DFARS citations from the response
function extractSources(text) {
  const sources = new Set();

  // Match FAR references
  const farMatches = text.match(/FAR\s+(?:Part\s+)?[\d.]+(?:\s+Subpart\s+[\d.]+)?/gi) || [];
  farMatches.forEach(m => sources.add(m));

  // Match DFARS references
  const dfarsMatches = text.match(/DFARS\s+[\d.]+/gi) || [];
  dfarsMatches.forEach(m => sources.add(m));

  // Match CFR references
  const cfrMatches = text.match(/\d+\s+CFR\s+[\d.]+/gi) || [];
  cfrMatches.forEach(m => sources.add(m));

  // Match SBA references
  if (text.toLowerCase().includes('sba') || text.toLowerCase().includes('small business')) {
    sources.add('SBA.gov');
  }

  // Match SAM.gov references
  if (text.toLowerCase().includes('sam.gov') || text.toLowerCase().includes('system for award management')) {
    sources.add('SAM.gov');
  }

  return Array.from(sources).slice(0, 5);
}

// Calculate confidence score based on response characteristics
function calculateConfidence(answer, question) {
  let score = 75; // Base confidence

  // Increase for longer, more detailed responses
  if (answer.length > 500) score += 5;
  if (answer.length > 1000) score += 5;

  // Increase for FAR/DFARS citations
  if (answer.match(/FAR\s+[\d.]+/gi)) score += 5;
  if (answer.match(/DFARS\s+[\d.]+/gi)) score += 3;

  // Decrease for uncertainty language
  if (answer.toLowerCase().includes("i'm not sure") ||
      answer.toLowerCase().includes("i don't have") ||
      answer.toLowerCase().includes("uncertain")) {
    score -= 10;
  }

  // Decrease for redirect responses (off-topic)
  if (answer.toLowerCase().includes("i specialize in government contracting")) {
    score = 50;
  }

  return Math.min(95, Math.max(50, score));
}

// Clean any remaining markdown from response
function cleanResponse(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, '$1')
    .replace(/__(.*?)__/g, '$1')
    .replace(/\*(.*?)\*/g, '$1')
    .replace(/_([^_\s][^_]*[^_\s])_/g, '$1')
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/^#{1,6}\s*/gm, '')
    .replace(/<think>[\s\S]*?<\/think>/gi, '')  // Remove DeepSeek thinking tags
    .trim();
}
