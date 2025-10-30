# Government Contracting Knowledge Base

An Apple-inspired, executive-level UI for querying government contracting documents using AI.

## 🎨 Design Features

- **Apple-level aesthetics**: Clean, minimal, professional design
- **No scrolling**: Everything visible on one page (fixed viewport)
- **Tabbed interface**: Switch between AI Assistant and Resource Library
- **Executive-ready**: Designed for high-level decision makers
- **Responsive**: Works on all screen sizes

## 🚀 Quick Start - View the UI

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
   - Or manually navigate to that URL

## 📋 What You'll See

### AI Assistant Tab
- **Welcome screen** with suggested questions
- **Chat interface** with beautiful message bubbles
- **Source citations** for every answer
- **Confidence indicators** to show answer reliability
- **Clean input** at the bottom (no scrolling needed)

### Resource Library Tab
- **Search bar** to find documents instantly
- **Category filters**: FAR, DFARS, Proposals, Templates, Guides
- **Document cards** in a responsive grid
- **Quick actions**: Download, Ask AI buttons
- **Stats bar** showing total documents

## 🎯 Current Status

✅ Beautiful UI complete (Apple-inspired design)
✅ Tabbed interface working
✅ Mock data for preview
⏳ Backend integration (Gemini API) - Next step
⏳ Vector database setup (Pinecone) - Next step
⏳ Document ingestion pipeline - Next step

## 📁 Project Structure

```
govcon-rag-chatbot/
├── app.py                 # Main Streamlit application (UI)
├── config.py             # Configuration settings
├── ingest_documents.py   # Document processing pipeline
├── requirements.txt      # Full dependencies
├── .env.example         # Environment variables template
└── documents/           # Place your 179 documents here
```

## 🔐 Setup (Coming Next)

Once you approve the UI, we'll add:
1. Your Google AI Studio API key
2. Pinecone vector database setup
3. Document ingestion from your 179 files
4. Real Gemini 2.0 Flash integration
5. Citation and source tracking

## 💡 Notes

- Currently showing **mock data** for UI preview
- AI responses are simulated (will be real once backend is connected)
- All 179 documents will appear in Resource Library once uploaded
- No data leaves your machine until APIs are configured

---

**Next Step:** Run the app and let me know if you love the design! 🎨
