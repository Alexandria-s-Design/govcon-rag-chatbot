"""
GovCon Intelligence - AI Chatbot
Clean, Modern Design - Built from Scratch
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="GovCon Intelligence",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Complete CSS Reset & New Design
st.markdown("""
<style>
    /* === FONTS === */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* === COMPLETE RESET === */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* === HIDE STREAMLIT ELEMENTS === */
    #MainMenu, footer, header, .stDeployButton {visibility: hidden; display: none;}
    section[data-testid="stSidebar"] {display: none;}

    /* === BASE STYLES === */
    html, body, [data-testid="stAppViewContainer"], .main {
        background: #0f0f0f;
        font-family: 'Inter', -apple-system, sans-serif;
        color: #ffffff;
    }

    .stApp {
        background: #0f0f0f;
    }

    /* === REMOVE ALL STREAMLIT PADDING === */
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* === LAYOUT === */
    .app-container {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
    }

    /* === HEADER === */
    .app-header {
        padding: 20px 40px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(15, 15, 15, 0.8);
        backdrop-filter: blur(20px);
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    .header-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .logo {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #a855f7, #6366f1);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.3);
    }

    .header-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
    }

    .header-subtitle {
        font-size: 13px;
        color: rgba(255, 255, 255, 0.5);
        margin-left: 4px;
    }

    /* === MAIN CHAT AREA === */
    .chat-container {
        flex: 1;
        max-width: 900px;
        width: 100%;
        margin: 0 auto;
        padding: 40px 20px;
        display: flex;
        flex-direction: column;
    }

    /* === MESSAGES === */
    .messages-wrapper {
        flex: 1;
        overflow-y: auto;
        padding: 20px;
        margin-bottom: 20px;
    }

    .messages-wrapper::-webkit-scrollbar {
        width: 6px;
    }

    .messages-wrapper::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }

    .message {
        margin-bottom: 30px;
        animation: fadeIn 0.3s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .message-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }

    .avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }

    .avatar-user {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
    }

    .avatar-ai {
        background: linear-gradient(135deg, #a855f7, #6366f1);
    }

    .message-role {
        font-size: 14px;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.9);
    }

    .message-content {
        margin-left: 48px;
        padding: 18px 20px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        line-height: 1.7;
        color: rgba(255, 255, 255, 0.9);
        font-size: 15px;
    }

    .message-user .message-content {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(37, 99, 235, 0.08));
        border-color: rgba(59, 130, 246, 0.3);
    }

    /* === SOURCES & CONFIDENCE === */
    .message-meta {
        margin-left: 48px;
        margin-top: 12px;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .source {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        background: rgba(168, 85, 247, 0.1);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 8px;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.8);
        width: fit-content;
        transition: all 0.2s;
    }

    .source:hover {
        background: rgba(168, 85, 247, 0.15);
        border-color: rgba(168, 85, 247, 0.4);
    }

    .confidence {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 12px;
        background: rgba(34, 197, 94, 0.12);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        color: #22c55e;
        width: fit-content;
    }

    /* === WELCOME SCREEN === */
    .welcome {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 60px 20px;
    }

    .welcome-icon {
        font-size: 72px;
        margin-bottom: 32px;
        background: linear-gradient(135deg, #a855f7, #6366f1, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 30px rgba(168, 85, 247, 0.4));
    }

    .welcome-title {
        font-size: 36px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }

    .welcome-subtitle {
        font-size: 17px;
        color: rgba(255, 255, 255, 0.6);
        max-width: 600px;
        line-height: 1.6;
        margin-bottom: 32px;
    }

    .suggestions {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        max-width: 700px;
    }

    .suggestion {
        padding: 12px 20px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 10px;
        color: rgba(255, 255, 255, 0.8);
        font-size: 14px;
        cursor: pointer;
        transition: all 0.2s;
    }

    .suggestion:hover {
        background: rgba(168, 85, 247, 0.15);
        border-color: rgba(168, 85, 247, 0.4);
        transform: translateY(-2px);
    }

    /* === INPUT AREA === */
    .input-container {
        position: sticky;
        bottom: 0;
        padding: 20px;
        background: rgba(15, 15, 15, 0.95);
        backdrop-filter: blur(20px);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .input-wrapper {
        max-width: 900px;
        margin: 0 auto;
        display: flex;
        gap: 12px;
        align-items: center;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 14px;
        padding: 6px;
        transition: all 0.3s;
    }

    .input-wrapper:focus-within {
        border-color: rgba(168, 85, 247, 0.5);
        box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.1);
    }

    /* === STREAMLIT INPUT STYLING === */
    .stTextInput {
        flex: 1;
    }

    .stTextInput > div > div {
        background: transparent !important;
        border: none !important;
    }

    .stTextInput input {
        background: transparent !important;
        border: none !important;
        color: #ffffff !important;
        font-size: 15px !important;
        padding: 12px 16px !important;
        outline: none !important;
        box-shadow: none !important;
    }

    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    .stTextInput label {
        display: none !important;
    }

    /* === BUTTON STYLING === */
    .stButton {
        margin: 0 !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #a855f7, #6366f1) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.2s !important;
        box-shadow: 0 4px 12px rgba(168, 85, 247, 0.3) !important;
        height: auto !important;
    }

    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4) !important;
    }

    .stButton button:active {
        transform: translateY(0px) !important;
    }

    /* === HIDE STREAMLIT ARTIFACTS === */
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }

    div[data-testid="column"] {
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# App Structure
st.markdown("""
<div class="app-container">
    <div class="app-header">
        <div class="header-content">
            <div class="logo">⚡</div>
            <div>
                <span class="header-title">GovCon Intelligence</span>
                <span class="header-subtitle">• Powered by Gemini 2.0 • 179 Documents</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Chat Container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Messages or Welcome Screen
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome">
        <div class="welcome-icon">⚡</div>
        <h1 class="welcome-title">Government Contracting Intelligence</h1>
        <p class="welcome-subtitle">
            Ask anything about FAR, DFARS, compliance requirements, or proposal development.
            Get accurate answers backed by 179 regulatory documents with citations.
        </p>
        <div class="suggestions">
            <div class="suggestion">Small business set-aside requirements</div>
            <div class="suggestion">FFP vs CPFF contract differences</div>
            <div class="suggestion">SAM.gov registration process</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="messages-wrapper">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            st.markdown(f"""
            <div class="message message-user">
                <div class="message-header">
                    <div class="avatar avatar-user">👤</div>
                    <div class="message-role">You</div>
                </div>
                <div class="message-content">{msg['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            sources_html = ""
            confidence_html = ""

            if 'sources' in msg and msg['sources']:
                sources_html = '<div class="message-meta">'
                for source in msg['sources']:
                    sources_html += f'<div class="source">📄 {source}</div>'

            if 'confidence' in msg:
                confidence_html = f'<div class="confidence">✓ {msg["confidence"]}% Confident</div>'

            if sources_html or confidence_html:
                sources_html += confidence_html + '</div>'

            st.markdown(f"""
            <div class="message message-ai">
                <div class="message-header">
                    <div class="avatar avatar-ai">🤖</div>
                    <div class="message-role">AI Assistant</div>
                </div>
                <div class="message-content">{msg['content']}</div>
                {sources_html}
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input Area (always at bottom)
st.markdown('<div class="input-container"><div class="input-wrapper">', unsafe_allow_html=True)

col1, col2 = st.columns([6, 1])
with col1:
    user_input = st.text_input("", placeholder="Ask anything about government contracting...", key="user_input")
with col2:
    send_button = st.button("Send")

st.markdown('</div></div>', unsafe_allow_html=True)

# Handle message sending
if send_button and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Mock AI response (replace with real Gemini later)
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Based on the Federal Acquisition Regulation (FAR) Part 19, small business set-asides are required when there's a reasonable expectation that at least two small business concerns will submit offers and that award will be made at fair market prices.",
        "sources": ["FAR_Part_19.docx", "SBA_Size_Standards.pdf"],
        "confidence": 94
    })

    st.rerun()
