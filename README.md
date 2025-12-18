# GovCon Intelligence

**Government Contracting Advisory Chatbot**

A professional, AI-powered chatbot designed to help small businesses navigate the complex world of federal government contracting. Get expert guidance on FAR, DFARS, contract types, compliance requirements, and proposal development.

## 🚀 Live Demo

**[Launch GovCon Intelligence →](https://alexandria-s-design.github.io/govcon-rag-chatbot/)**

## ✨ Features

### Comprehensive Knowledge Base
- **179 regulatory documents** covering FAR, DFARS, and agency-specific supplements
- **Real-time answers** with citations and confidence scores
- **Expert guidance** on SAM.gov registration, SBIR/STTR programs, GSA schedules, and contract types

### Professional Interface
- **Editorial design** inspired by high-end consulting portals
- **Quick topic sidebar** for common questions
- **Source citations** for every response
- **Confidence indicators** showing answer reliability
- **Mobile responsive** design for on-the-go access

### Key Topics Covered

#### Getting Started
- SAM.gov registration process and requirements
- Small business set-aside requirements
- SBIR vs STTR program differences
- Size standard determinations

#### Contract Types
- Firm-Fixed-Price (FFP) contracts
- Time & Materials (T&M) contracts
- Cost-Plus-Fixed-Fee (CPFF) contracts
- Contract type selection guidance

#### Compliance & Regulations
- FAR Part 19 small business requirements
- DFARS cybersecurity requirements (NIST 800-171, CMMC)
- GSA Schedule certification requirements
- Trade Agreements Act compliance

#### Proposal Development
- Technical proposal structure and content
- Cost proposal pricing strategies
- Past performance documentation
- Evaluation criteria and scoring

## 🎯 Built For

- **Small businesses** entering government contracting
- **Proposal teams** seeking quick regulatory guidance
- **Compliance officers** verifying requirements
- **Business development** professionals researching opportunities

## 💡 How It Works

1. **Ask a question** about any aspect of government contracting
2. **Get expert answers** backed by regulatory citations
3. **Review sources** to verify information
4. **Follow quick topics** for common scenarios

The chatbot uses intelligent keyword matching against a comprehensive knowledge base of government contracting regulations, policies, and best practices.

## 🛠️ Technology Stack

- **Frontend**: Pure HTML/CSS/JavaScript (no dependencies)
- **Design**: Custom editorial aesthetic (Crimson Pro + DM Sans typography)
- **Hosting**: GitHub Pages
- **Performance**: Instant responses, no backend required

## 📚 Knowledge Sources

The chatbot provides guidance based on:
- Federal Acquisition Regulation (FAR)
- Defense Federal Acquisition Regulation Supplement (DFARS)
- General Services Administration Acquisition Manual (GSAM)
- SBA regulations and size standards
- SBIR/STTR program directives
- GSA Schedule policies
- Industry best practices

## 🚧 Future Enhancements

### Backend Integration (Planned)
- **Google Gemini 2.0 Flash** for advanced natural language understanding
- **Pinecone vector database** for semantic search across all documents
- **Document ingestion pipeline** for continuous knowledge base updates
- **Real-time regulatory updates** as new guidance is published

### Additional Features
- Saved conversation history
- Document export (PDF summaries)
- Personalized recommendations based on business profile
- Integration with SAM.gov API for real-time data

## 🔐 Privacy & Security

- All data processing occurs client-side (current version)
- No personal information collected or stored
- No tracking or analytics
- Open source and transparent

## 📖 Usage Example

**Question**: "What are the requirements for small business set-aside contracts?"

**Response**: Detailed explanation covering:
- FAR Part 19 eligibility criteria
- Types of set-asides (8(a), HUBZone, WOSB, SDVOSB)
- Competitive requirements
- Limitations on subcontracting

**Sources**: FAR Part 19, SBA Size Standards, 13 CFR Part 121

**Confidence**: 97%

## 🤝 Contributing

This chatbot is designed to help small businesses succeed in government contracting. If you find inaccuracies or have suggestions for improvement, please open an issue or submit a pull request.

## ⚖️ Disclaimer

This chatbot provides general guidance based on publicly available regulations. It is **not** a substitute for:
- Legal advice from a government contracts attorney
- Official guidance from contracting officers
- Formal training or certification programs
- Professional consulting services

Always verify critical information with authoritative sources and seek professional advice for specific situations.

## 📞 Resources

- **FAR**: [acquisition.gov](https://www.acquisition.gov/browse/index/far)
- **DFARS**: [DFARS Home](https://www.acq.osd.mil/dpap/dars/dfarspgi/current/index.html)
- **SAM.gov**: [System for Award Management](https://sam.gov/)
- **SBIR/STTR**: [SBIR.gov](https://www.sbir.gov/)
- **PTAC Locator**: [Find your local PTAC](https://www.aptac-us.org/)

---

## 🖥️ Local Development (Streamlit Version)

The repository also includes a Streamlit version for local development:

### Quick Start

1. **Install dependencies:**
   ```bash
   pip install streamlit
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Open in browser:**
   - The app will automatically open at `http://localhost:8501`

### Project Structure

```
govcon-rag-chatbot/
├── index.html            # GitHub Pages version (live demo)
├── app.py                # Streamlit application (local dev)
├── config.py             # Configuration settings
├── ingest_documents.py   # Document processing pipeline
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── documents/           # Place your 179 documents here
```

## 📄 License

MIT License - Feel free to use this chatbot for your own projects.

---

**Built by Alexandria's Design** | Helping small businesses navigate government contracting since 2015
