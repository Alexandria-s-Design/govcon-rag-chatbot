"""
Configuration settings for the Government Contracting RAG Chatbot
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "gcp-starter")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "govcon-docs")

# Model Configuration
GEMINI_MODEL = "gemini-2.0-flash-exp"  # Using latest Gemini 2.0 Flash
EMBEDDING_MODEL = "models/embedding-001"  # Google's embedding model

# Document Processing
CHUNK_SIZE = 1000  # Characters per chunk
CHUNK_OVERLAP = 200  # Overlap between chunks
DOCUMENTS_FOLDER = "documents"

# RAG Settings
TOP_K_RESULTS = 5  # Number of relevant chunks to retrieve
TEMPERATURE = 0.1  # Lower = more deterministic (important for accuracy)
MAX_OUTPUT_TOKENS = 2048

# UI Settings
PAGE_TITLE = "Government Contracting Knowledge Base"
PAGE_ICON = "📋"

# Accuracy Settings (for government contracting)
CONFIDENCE_THRESHOLD = 0.7  # Minimum similarity score to consider
REQUIRE_CITATIONS = True  # Always cite sources
ENABLE_UNCERTAINTY_RESPONSE = True  # Bot should say "I don't know" when uncertain
