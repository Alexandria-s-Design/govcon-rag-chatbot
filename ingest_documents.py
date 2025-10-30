"""
Document Ingestion Pipeline for Government Contracting Documents
Processes Word/Text documents and stores them in vector database
"""
import os
import sys
from pathlib import Path
from typing import List
import docx
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from pinecone import Pinecone, ServerlessSpec
import config

def read_docx(file_path: str) -> str:
    """Extract text from a Word document"""
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def read_txt(file_path: str) -> str:
    """Read plain text file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def load_documents(folder_path: str) -> List[dict]:
    """Load all documents from the specified folder"""
    documents = []
    folder = Path(folder_path)

    if not folder.exists():
        print(f"Creating documents folder: {folder_path}")
        folder.mkdir(parents=True, exist_ok=True)
        print(f"Please place your 179 documents in: {folder.absolute()}")
        return documents

    # Supported file extensions
    supported_extensions = ['.docx', '.txt', '.doc']

    for file_path in folder.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            print(f"Processing: {file_path.name}")

            # Read content based on file type
            if file_path.suffix.lower() == '.docx':
                content = read_docx(str(file_path))
            else:
                content = read_txt(str(file_path))

            if content:
                documents.append({
                    'content': content,
                    'metadata': {
                        'source': file_path.name,
                        'file_path': str(file_path),
                        'file_type': file_path.suffix
                    }
                })

    print(f"\nTotal documents loaded: {len(documents)}")
    return documents

def chunk_documents(documents: List[dict]) -> List[dict]:
    """Split documents into smaller chunks for better retrieval"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunked_docs = []
    for doc in documents:
        chunks = text_splitter.split_text(doc['content'])
        for i, chunk in enumerate(chunks):
            chunked_docs.append({
                'content': chunk,
                'metadata': {
                    **doc['metadata'],
                    'chunk_id': i,
                    'total_chunks': len(chunks)
                }
            })

    print(f"Total chunks created: {len(chunked_docs)}")
    return chunked_docs

def setup_pinecone():
    """Initialize Pinecone index"""
    if not config.PINECONE_API_KEY:
        print("ERROR: PINECONE_API_KEY not found in .env file")
        sys.exit(1)

    pc = Pinecone(api_key=config.PINECONE_API_KEY)

    # Check if index exists
    existing_indexes = pc.list_indexes().names()

    if config.PINECONE_INDEX_NAME not in existing_indexes:
        print(f"Creating new Pinecone index: {config.PINECONE_INDEX_NAME}")
        pc.create_index(
            name=config.PINECONE_INDEX_NAME,
            dimension=768,  # Google's embedding-001 dimension
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print("Index created successfully!")
    else:
        print(f"Using existing index: {config.PINECONE_INDEX_NAME}")

    return pc

def ingest_to_vectorstore(chunked_docs: List[dict]):
    """Store chunked documents in Pinecone vector database"""
    if not config.GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not found in .env file")
        sys.exit(1)

    # Initialize embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model=config.EMBEDDING_MODEL,
        google_api_key=config.GOOGLE_API_KEY
    )

    # Setup Pinecone
    pc = setup_pinecone()

    # Prepare documents for LangChain
    texts = [doc['content'] for doc in chunked_docs]
    metadatas = [doc['metadata'] for doc in chunked_docs]

    print("\nIngesting documents to Pinecone (this may take a few minutes)...")

    # Create vector store
    vectorstore = LangchainPinecone.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        index_name=config.PINECONE_INDEX_NAME
    )

    print("✓ Documents successfully ingested to Pinecone!")
    return vectorstore

def main():
    """Main ingestion pipeline"""
    print("=" * 60)
    print("Government Contracting Document Ingestion Pipeline")
    print("=" * 60)

    # Load documents
    print(f"\nStep 1: Loading documents from '{config.DOCUMENTS_FOLDER}'...")
    documents = load_documents(config.DOCUMENTS_FOLDER)

    if not documents:
        print("\nNo documents found. Please add your 179 documents to the 'documents' folder.")
        print("Supported formats: .docx, .txt, .doc")
        return

    # Chunk documents
    print("\nStep 2: Chunking documents...")
    chunked_docs = chunk_documents(documents)

    # Ingest to vector store
    print("\nStep 3: Ingesting to Pinecone vector database...")
    ingest_to_vectorstore(chunked_docs)

    print("\n" + "=" * 60)
    print("✓ Ingestion Complete!")
    print("=" * 60)
    print("\nYou can now run the chatbot with: streamlit run app.py")

if __name__ == "__main__":
    main()
