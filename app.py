"""
Government Contracting Knowledge Base
Premium Executive UI - Inspired by Linear, Stripe, Vercel
"""
import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="GovCon Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium CSS Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* === RESET & BASE === */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: #0a0a0a;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        overflow: hidden;
        height: 100vh;
    }

    .main .block-container {
        padding: 0;
        max-width: 100%;
        height: 100vh;
        overflow: hidden;
    }

    /* === PREMIUM HEADER === */
    .premium-header {
        position: relative;
        background: linear-gradient(to bottom, rgba(10, 10, 10, 0.95), rgba(10, 10, 10, 0.85));
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px 48px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 100;
    }

    .premium-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.5), transparent);
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .brand-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
    }

    .brand-text h1 {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.5px;
        margin: 0;
    }

    .brand-text p {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.5);
        margin: 2px 0 0 0;
    }

    .tab-switcher {
        display: flex;
        gap: 6px;
        background: rgba(255, 255, 255, 0.05);
        padding: 4px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .tab-btn {
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.6);
        background: transparent;
        border: none;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .tab-btn.active {
        color: #ffffff;
        background: rgba(139, 92, 246, 0.2);
        border: 1px solid rgba(139, 92, 246, 0.3);
    }

    .tab-btn.active::before {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(99, 102, 241, 0.1));
    }

    /* === MAIN CONTENT AREA === */
    .content-wrapper {
        height: calc(100vh - 96px);
        padding: 32px 48px 48px;
        overflow: hidden;
    }

    /* === CHAT INTERFACE === */
    .chat-layout {
        display: flex;
        flex-direction: column;
        height: 100%;
        gap: 20px;
    }

    .messages-area {
        flex: 1;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 40px;
        overflow-y: auto;
        position: relative;
    }

    .messages-area::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 100px;
        background: linear-gradient(to bottom, rgba(139, 92, 246, 0.05), transparent);
        border-radius: 20px 20px 0 0;
        pointer-events: none;
    }

    .messages-area::-webkit-scrollbar {
        width: 8px;
    }

    .messages-area::-webkit-scrollbar-track {
        background: transparent;
    }

    .messages-area::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border: 2px solid transparent;
        background-clip: padding-box;
    }

    .messages-area::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.2);
        background-clip: padding-box;
    }

    /* === WELCOME STATE === */
    .welcome-state {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        text-align: center;
        gap: 32px;
        position: relative;
    }

    .welcome-hero {
        font-size: 72px;
        background: linear-gradient(135deg, #8b5cf6, #6366f1, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 30px rgba(139, 92, 246, 0.5));
    }

    .welcome-heading {
        font-size: 36px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -1px;
        line-height: 1.2;
        margin: 0;
    }

    .welcome-subheading {
        font-size: 17px;
        color: rgba(255, 255, 255, 0.6);
        max-width: 600px;
        line-height: 1.7;
        margin: 0;
    }

    .quick-prompts {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 12px;
    }

    .quick-prompt {
        padding: 14px 24px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }

    .quick-prompt:hover {
        background: rgba(139, 92, 246, 0.15);
        border-color: rgba(139, 92, 246, 0.4);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.2);
    }

    /* === MESSAGE BUBBLES === */
    .msg-wrapper {
        display: flex;
        gap: 20px;
        margin-bottom: 32px;
        animation: slideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .msg-avatar {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        flex-shrink: 0;
        position: relative;
    }

    .user-avatar {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }

    .ai-avatar {
        background: linear-gradient(135deg, #8b5cf6, #6366f1);
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
    }

    .msg-body {
        flex: 1;
        max-width: 70%;
    }

    .msg-bubble {
        padding: 20px 24px;
        border-radius: 16px;
        font-size: 15px;
        line-height: 1.7;
        position: relative;
    }

    .user-bubble {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(37, 99, 235, 0.1));
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #ffffff;
    }

    .ai-bubble {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.9);
    }

    /* === SOURCE CITATIONS === */
    .sources-section {
        margin-top: 16px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .source-tag {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 16px;
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 10px;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.8);
        cursor: pointer;
        transition: all 0.3s ease;
        width: fit-content;
    }

    .source-tag:hover {
        background: rgba(139, 92, 246, 0.2);
        border-color: rgba(139, 92, 246, 0.4);
        transform: translateX(4px);
    }

    .confidence-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 8px;
        font-size: 12px;
        font-weight: 600;
        color: #22c55e;
        margin-top: 12px;
        width: fit-content;
    }

    /* === INPUT AREA === */
    .input-zone {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 8px;
        display: flex;
        gap: 12px;
        align-items: center;
        transition: all 0.3s ease;
    }

    .input-zone:focus-within {
        border-color: rgba(139, 92, 246, 0.5);
        box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.1);
    }

    .stTextInput input {
        background: transparent !important;
        border: none !important;
        color: #ffffff !important;
        font-size: 15px !important;
        padding: 16px 20px !important;
        box-shadow: none !important;
    }

    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    .stTextInput input:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    .stTextInput > label {
        display: none;
    }

    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 32px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4) !important;
    }

    /* === RESOURCES GRID === */
    .resources-layout {
        display: flex;
        flex-direction: column;
        height: 100%;
        gap: 24px;
    }

    .resources-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
    }

    .search-container {
        flex: 1;
        position: relative;
    }

    .search-icon {
        position: absolute;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        color: rgba(255, 255, 255, 0.4);
        font-size: 18px;
    }

    .filters-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }

    .filter-tag {
        padding: 12px 24px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        font-size: 14px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.7);
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .filter-tag:hover {
        background: rgba(139, 92, 246, 0.15);
        border-color: rgba(139, 92, 246, 0.4);
        color: #ffffff;
    }

    .filter-tag.active {
        background: linear-gradient(135deg, #8b5cf6, #6366f1);
        border-color: transparent;
        color: #ffffff;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
    }

    /* === RESOURCE CARDS === */
    .resources-grid {
        flex: 1;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        overflow-y: auto;
        padding: 4px;
    }

    .resources-grid::-webkit-scrollbar {
        width: 8px;
    }

    .resources-grid::-webkit-scrollbar-track {
        background: transparent;
    }

    .resources-grid::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }

    .doc-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 28px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        height: fit-content;
    }

    .doc-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #8b5cf6, #6366f1, #3b82f6);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }

    .doc-card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(139, 92, 246, 0.4);
        transform: translateY(-6px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }

    .doc-card:hover::before {
        transform: scaleX(1);
    }

    .doc-icon {
        width: 56px;
        height: 56px;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(99, 102, 241, 0.2));
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin-bottom: 20px;
    }

    .doc-title {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
        line-height: 1.3;
    }

    .doc-desc {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.6);
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .doc-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 16px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        font-size: 12px;
        color: rgba(255, 255, 255, 0.5);
    }

    .doc-actions {
        display: flex;
        gap: 8px;
        margin-top: 16px;
    }

    .doc-btn {
        flex: 1;
        padding: 10px 18px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        font-size: 13px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.8);
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
    }

    .doc-btn:hover {
        background: rgba(139, 92, 246, 0.2);
        border-color: rgba(139, 92, 246, 0.4);
        color: #ffffff;
    }

    /* === STATS BAR === */
    .stats-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 28px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'chat'
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'selected_filter' not in st.session_state:
    st.session_state.selected_filter = 'All'

# Mock data
MOCK_RESOURCES = [
    {"title": "FAR Part 19", "description": "Small Business Programs and comprehensive Set-Asides regulations", "type": "DOCX", "size": "1.2 MB", "date": "Oct 2024", "emoji": "📘"},
    {"title": "DFARS 252.204", "description": "Defense Contract Clauses and Provisions documentation", "type": "PDF", "size": "2.8 MB", "date": "Sep 2024", "emoji": "📗"},
    {"title": "SBA Size Standards", "description": "Complete Small Business Size Determination Guide", "type": "PDF", "size": "856 KB", "date": "Oct 2024", "emoji": "📊"},
    {"title": "Proposal Template", "description": "Technical Proposal Writing Best Practices and examples", "type": "DOCX", "size": "445 KB", "date": "Aug 2024", "emoji": "📝"},
    {"title": "Cost Estimating", "description": "Government Cost and Price Analysis comprehensive guide", "type": "PDF", "size": "1.5 MB", "date": "Sep 2024", "emoji": "💰"},
    {"title": "FAR Part 15", "description": "Contracting by Negotiation Procedures and requirements", "type": "DOCX", "size": "1.8 MB", "date": "Oct 2024", "emoji": "📋"},
]

# Header
st.markdown("""
<div class="premium-header">
    <div class="brand">
        <div class="brand-icon">⚡</div>
        <div class="brand-text">
            <h1>GovCon Intelligence</h1>
            <p>Powered by Gemini 2.0 • 179 Documents</p>
        </div>
    </div>
    <div class="tab-switcher">
        <button class="tab-btn {}">💬 AI Assistant</button>
        <button class="tab-btn {}">📚 Resources</button>
    </div>
</div>
""".format(
    'active' if st.session_state.active_tab == 'chat' else '',
    'active' if st.session_state.active_tab == 'resources' else ''
), unsafe_allow_html=True)

# Tab buttons
col1, col2, col_spacer = st.columns([1, 1, 6])
with col1:
    if st.button("💬 AI Assistant", use_container_width=True, key="tab_chat"):
        st.session_state.active_tab = 'chat'
        st.rerun()
with col2:
    if st.button("📚 Resources", use_container_width=True, key="tab_resources"):
        st.session_state.active_tab = 'resources'
        st.rerun()

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# === CHAT TAB ===
if st.session_state.active_tab == 'chat':
    st.markdown('<div class="chat-layout">', unsafe_allow_html=True)
    st.markdown('<div class="messages-area">', unsafe_allow_html=True)

    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div class="welcome-state">
            <div class="welcome-hero">⚡</div>
            <h1 class="welcome-heading">Your Government Contracting<br/>Intelligence Hub</h1>
            <p class="welcome-subheading">
                Ask anything about FAR, DFARS, compliance requirements, or proposal development.
                Get accurate answers backed by your 179 regulatory documents.
            </p>
            <div class="quick-prompts">
                <div class="quick-prompt">Small business set-aside requirements</div>
                <div class="quick-prompt">FFP vs CPFF contract differences</div>
                <div class="quick-prompt">SAM.gov registration process</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                st.markdown(f"""
                <div class="msg-wrapper">
                    <div class="msg-avatar user-avatar">👤</div>
                    <div class="msg-body">
                        <div class="msg-bubble user-bubble">{msg['content']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                sources_html = ""
                if 'sources' in msg:
                    sources_html = '<div class="sources-section">'
                    for source in msg['sources']:
                        sources_html += f'<div class="source-tag">📄 {source}</div>'
                    sources_html += '</div>'

                confidence_html = ""
                if 'confidence' in msg:
                    confidence_html = f'<div class="confidence-badge">✓ {msg["confidence"]}% Confident</div>'

                st.markdown(f"""
                <div class="msg-wrapper">
                    <div class="msg-avatar ai-avatar">🤖</div>
                    <div class="msg-body">
                        <div class="msg-bubble ai-bubble">{msg['content']}</div>
                        {sources_html}
                        {confidence_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Input area
    st.markdown('<div class="input-zone">', unsafe_allow_html=True)
    col1, col2 = st.columns([8, 1])
    with col1:
        user_input = st.text_input("", placeholder="Ask anything about government contracting...", label_visibility="collapsed", key="chat_input")
    with col2:
        send_btn = st.button("Send", use_container_width=True, key="send")

    if send_btn and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Based on the Federal Acquisition Regulation (FAR) Part 19, small business set-asides are required when there's a reasonable expectation that at least two small business concerns will submit offers and that award will be made at fair market prices.",
            "sources": ["FAR_Part_19.docx", "SBA_Size_Standards.pdf"],
            "confidence": 94
        })
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# === RESOURCES TAB ===
else:
    st.markdown('<div class="resources-layout">', unsafe_allow_html=True)

    # Header
    st.markdown('<div class="resources-header">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        search_input = st.text_input("", placeholder="🔍 Search 179 documents...", label_visibility="collapsed", key="search")
    st.markdown('</div>', unsafe_allow_html=True)

    # Filters
    st.markdown('<div class="filters-row">', unsafe_allow_html=True)
    filters = ['All', 'FAR', 'DFARS', 'Proposals', 'Templates', 'Guides']
    cols = st.columns(len(filters))
    for idx, f in enumerate(filters):
        with cols[idx]:
            if st.button(f, key=f"filter_{f}", use_container_width=True):
                st.session_state.selected_filter = f
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Grid
    st.markdown('<div class="resources-grid">', unsafe_allow_html=True)
    for doc in MOCK_RESOURCES:
        st.markdown(f"""
        <div class="doc-card">
            <div class="doc-icon">{doc['emoji']}</div>
            <div class="doc-title">{doc['title']}</div>
            <div class="doc-desc">{doc['description']}</div>
            <div class="doc-meta">
                <span>{doc['type']} • {doc['size']}</span>
                <span>{doc['date']}</span>
            </div>
            <div class="doc-actions">
                <div class="doc-btn">📥 Download</div>
                <div class="doc-btn">💬 Ask AI</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(f"""
    <div class="stats-footer">
        <span>Showing {len(MOCK_RESOURCES)} of 179 documents</span>
        <span>Last updated: Today</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
