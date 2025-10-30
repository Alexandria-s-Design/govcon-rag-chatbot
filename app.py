"""
Government Contracting Knowledge Base
Apple-inspired UI for Executive Use
"""
import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="GovCon Knowledge Base",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Apple-inspired design
st.markdown("""
<style>
    /* Import SF Pro-like font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Remove default Streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Reset and base styles */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        overflow: hidden;
        height: 100vh;
    }

    /* Main container - fixed viewport */
    .main .block-container {
        padding: 0;
        max-width: 100%;
        height: 100vh;
        overflow: hidden;
    }

    /* Header */
    .app-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 20px 48px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }

    .app-title {
        font-size: 24px;
        font-weight: 600;
        color: #1d1d1f;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .app-subtitle {
        font-size: 13px;
        font-weight: 400;
        color: #86868b;
        margin-top: 2px;
    }

    /* Tab Navigation */
    .tab-container {
        display: flex;
        gap: 8px;
        background: rgba(255, 255, 255, 0.6);
        padding: 6px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
    }

    .tab-button {
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        border: none;
        background: transparent;
        color: #1d1d1f;
    }

    .tab-button.active {
        background: white;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        color: #0071e3;
    }

    /* Content Area - Fixed Height */
    .content-area {
        height: calc(100vh - 85px);
        padding: 32px 48px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    /* Chat Interface */
    .chat-container {
        display: flex;
        flex-direction: column;
        height: 100%;
        gap: 24px;
    }

    .chat-messages {
        flex: 1;
        background: white;
        border-radius: 16px;
        padding: 32px;
        overflow-y: auto;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    /* Custom scrollbar */
    .chat-messages::-webkit-scrollbar {
        width: 6px;
    }

    .chat-messages::-webkit-scrollbar-track {
        background: transparent;
    }

    .chat-messages::-webkit-scrollbar-thumb {
        background: rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }

    .chat-messages::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 0, 0, 0.2);
    }

    /* Message Bubbles */
    .message {
        display: flex;
        gap: 16px;
        animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .message-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }

    .message-content {
        flex: 1;
        max-width: 75%;
    }

    .message-bubble {
        padding: 16px 20px;
        border-radius: 18px;
        font-size: 15px;
        line-height: 1.6;
        color: #1d1d1f;
    }

    .user-message .message-bubble {
        background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
        color: white;
        border-bottom-right-radius: 4px;
    }

    .assistant-message .message-bubble {
        background: #f5f5f7;
        border-bottom-left-radius: 4px;
    }

    /* Source Citations */
    .message-sources {
        margin-top: 12px;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .source-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        background: white;
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 10px;
        font-size: 13px;
        color: #6e6e73;
        cursor: pointer;
        transition: all 0.2s ease;
        width: fit-content;
    }

    .source-chip:hover {
        border-color: #0071e3;
        color: #0071e3;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(0, 113, 227, 0.1);
    }

    .confidence-indicator {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        background: rgba(0, 113, 227, 0.08);
        border-radius: 8px;
        font-size: 12px;
        font-weight: 500;
        color: #0071e3;
        margin-top: 8px;
        width: fit-content;
    }

    /* Input Area */
    .chat-input-container {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        display: flex;
        gap: 12px;
        align-items: center;
    }

    .stTextInput input {
        border: none !important;
        font-size: 15px !important;
        padding: 14px 0 !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    .stTextInput input:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* Resources Grid */
    .resources-container {
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    .resources-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
    }

    .search-bar {
        flex: 1;
        background: white;
        border-radius: 12px;
        padding: 14px 20px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .filter-chips {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }

    .filter-chip {
        padding: 10px 20px;
        background: white;
        border: 1.5px solid rgba(0, 0, 0, 0.08);
        border-radius: 10px;
        font-size: 14px;
        font-weight: 500;
        color: #1d1d1f;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .filter-chip.active {
        background: #0071e3;
        color: white;
        border-color: #0071e3;
    }

    .filter-chip:hover {
        border-color: #0071e3;
        transform: translateY(-1px);
    }

    /* Resource Grid */
    .resources-grid {
        flex: 1;
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 20px;
        overflow-y: auto;
        padding: 4px;
    }

    .resource-card {
        background: white;
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        gap: 12px;
        height: fit-content;
    }

    .resource-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }

    .resource-icon {
        width: 48px;
        height: 48px;
        background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }

    .resource-title {
        font-size: 16px;
        font-weight: 600;
        color: #1d1d1f;
        line-height: 1.4;
    }

    .resource-description {
        font-size: 13px;
        color: #6e6e73;
        line-height: 1.5;
        flex: 1;
    }

    .resource-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        color: #86868b;
        padding-top: 8px;
        border-top: 1px solid rgba(0, 0, 0, 0.06);
    }

    .resource-actions {
        display: flex;
        gap: 8px;
        margin-top: 8px;
    }

    .resource-button {
        flex: 1;
        padding: 8px 16px;
        background: #f5f5f7;
        border: none;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 500;
        color: #1d1d1f;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .resource-button:hover {
        background: #0071e3;
        color: white;
    }

    /* Stats Bar */
    .stats-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 24px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        font-size: 13px;
        color: #6e6e73;
    }

    /* Welcome Screen */
    .welcome-screen {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        text-align: center;
        gap: 24px;
    }

    .welcome-icon {
        font-size: 64px;
        opacity: 0.5;
    }

    .welcome-title {
        font-size: 28px;
        font-weight: 600;
        color: #1d1d1f;
        letter-spacing: -0.5px;
    }

    .welcome-subtitle {
        font-size: 16px;
        color: #6e6e73;
        max-width: 500px;
        line-height: 1.6;
    }

    .suggestion-chips {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 16px;
    }

    .suggestion-chip {
        padding: 12px 20px;
        background: white;
        border: 1.5px solid rgba(0, 0, 0, 0.08);
        border-radius: 12px;
        font-size: 14px;
        color: #1d1d1f;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .suggestion-chip:hover {
        border-color: #0071e3;
        color: #0071e3;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 113, 227, 0.15);
    }

    /* Hide Streamlit elements */
    .stTextInput > label {
        display: none;
    }

    .stButton > button {
        background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0, 113, 227, 0.2);
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 113, 227, 0.3);
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

# Mock data for resources
MOCK_RESOURCES = [
    {"title": "FAR Part 19", "description": "Small Business Programs and Set-Asides", "type": "DOCX", "size": "1.2 MB", "date": "Oct 2024"},
    {"title": "DFARS 252.204", "description": "Defense Contract Clauses and Provisions", "type": "PDF", "size": "2.8 MB", "date": "Sep 2024"},
    {"title": "SBA Size Standards", "description": "Small Business Size Determination Guide", "type": "PDF", "size": "856 KB", "date": "Oct 2024"},
    {"title": "Proposal Template", "description": "Technical Proposal Writing Best Practices", "type": "DOCX", "size": "445 KB", "date": "Aug 2024"},
    {"title": "Cost Estimating", "description": "Government Cost and Price Analysis Guide", "type": "PDF", "size": "1.5 MB", "date": "Sep 2024"},
    {"title": "FAR Part 15", "description": "Contracting by Negotiation Procedures", "type": "DOCX", "size": "1.8 MB", "date": "Oct 2024"},
    {"title": "SAM Registration", "description": "System for Award Management Quick Guide", "type": "PDF", "size": "623 KB", "date": "Nov 2024"},
    {"title": "CPARS Guide", "description": "Contractor Performance Assessment", "type": "DOCX", "size": "782 KB", "date": "Sep 2024"},
    {"title": "Contract Types", "description": "FFP, CPFF, T&M Contract Overview", "type": "PDF", "size": "1.1 MB", "date": "Oct 2024"},
]

# Header
st.markdown("""
<div class="app-header">
    <div>
        <div class="app-title">
            <span>📋</span>
            <span>Government Contracting Knowledge Base</span>
        </div>
        <div class="app-subtitle">Powered by Gemini 2.0 Flash • 179 Documents</div>
    </div>
    <div class="tab-container">
        <button class="tab-button {}" onclick="window.location.href='?tab=chat'">
            💬 AI Assistant
        </button>
        <button class="tab-button {}" onclick="window.location.href='?tab=resources'">
            📚 Resource Library
        </button>
    </div>
</div>
""".format(
    'active' if st.session_state.active_tab == 'chat' else '',
    'active' if st.session_state.active_tab == 'resources' else ''
), unsafe_allow_html=True)

# Tab selector (using columns for interactivity)
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    if st.button("💬 AI Assistant", use_container_width=True):
        st.session_state.active_tab = 'chat'
        st.rerun()
with col2:
    if st.button("📚 Resource Library", use_container_width=True):
        st.session_state.active_tab = 'resources'
        st.rerun()

st.markdown('<div class="content-area">', unsafe_allow_html=True)

# === CHAT TAB ===
if st.session_state.active_tab == 'chat':
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Messages container
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)

    if len(st.session_state.messages) == 0:
        # Welcome screen
        st.markdown("""
        <div class="welcome-screen">
            <div class="welcome-icon">🤖</div>
            <div class="welcome-title">Welcome to Your GovCon Assistant</div>
            <div class="welcome-subtitle">
                I'm here to help you navigate government contracting regulations,
                compliance requirements, and proposal development. Ask me anything about
                FAR, DFARS, or contracting procedures.
            </div>
            <div class="suggestion-chips">
                <div class="suggestion-chip">What are small business set-aside requirements?</div>
                <div class="suggestion-chip">Explain FFP vs CPFF contracts</div>
                <div class="suggestion-chip">How do I register in SAM.gov?</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Display messages
        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                st.markdown(f"""
                <div class="message user-message">
                    <div class="message-avatar" style="background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%); color: white;">👤</div>
                    <div class="message-content">
                        <div class="message-bubble">{msg['content']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                sources_html = ""
                if 'sources' in msg:
                    sources_html = '<div class="message-sources">'
                    for source in msg['sources']:
                        sources_html += f'<div class="source-chip">📄 {source}</div>'
                    sources_html += '</div>'

                confidence_html = ""
                if 'confidence' in msg:
                    confidence_html = f'<div class="confidence-indicator">🎯 {msg["confidence"]}% Confident</div>'

                st.markdown(f"""
                <div class="message assistant-message">
                    <div class="message-avatar" style="background: #f5f5f7;">🤖</div>
                    <div class="message-content">
                        <div class="message-bubble">{msg['content']}</div>
                        {sources_html}
                        {confidence_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close chat-messages

    # Input area
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([9, 1])
    with col1:
        user_input = st.text_input("Message", placeholder="Ask me anything about government contracting...", label_visibility="collapsed", key="chat_input")
    with col2:
        send_button = st.button("Send", use_container_width=True)

    if send_button and user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Simulate AI response (replace with actual Gemini call later)
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Based on the Federal Acquisition Regulation (FAR) Part 19, small business set-asides are required when there's a reasonable expectation that at least two small business concerns will submit offers and that award will be made at fair market prices.",
            "sources": ["FAR_Part_19.docx", "SBA_Size_Standards.pdf"],
            "confidence": 94
        })

        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)  # Close input container
    st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container

# === RESOURCES TAB ===
else:
    st.markdown('<div class="resources-container">', unsafe_allow_html=True)

    # Search and filter header
    st.markdown('<div class="resources-header">', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        search_query = st.text_input("Search", placeholder="🔍 Search 179 documents...", label_visibility="collapsed", key="search")

    st.markdown('</div>', unsafe_allow_html=True)

    # Filter chips
    st.markdown('<div class="filter-chips">', unsafe_allow_html=True)
    filters = ['All', 'FAR', 'DFARS', 'Proposals', 'Templates', 'Guides']
    cols = st.columns(len(filters))
    for idx, filter_name in enumerate(filters):
        with cols[idx]:
            if st.button(filter_name, key=f"filter_{filter_name}", use_container_width=True):
                st.session_state.selected_filter = filter_name
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Resource grid
    st.markdown('<div class="resources-grid">', unsafe_allow_html=True)

    for resource in MOCK_RESOURCES:
        file_emoji = "📄" if resource['type'] == 'PDF' else "📝"
        st.markdown(f"""
        <div class="resource-card">
            <div class="resource-icon">{file_emoji}</div>
            <div class="resource-title">{resource['title']}</div>
            <div class="resource-description">{resource['description']}</div>
            <div class="resource-meta">
                <span>{resource['type']} • {resource['size']}</span>
                <span>{resource['date']}</span>
            </div>
            <div class="resource-actions">
                <button class="resource-button">📥 Download</button>
                <button class="resource-button">💬 Ask AI</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close resources-grid

    # Stats bar
    st.markdown("""
    <div class="stats-bar">
        <span>Showing 9 of 179 documents</span>
        <span>Last updated: Today • {} documents</span>
    </div>
    """.format(len(MOCK_RESOURCES)), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close resources-container

st.markdown('</div>', unsafe_allow_html=True)  # Close content-area
