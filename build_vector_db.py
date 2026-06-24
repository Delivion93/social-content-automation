from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents():

    documents = []

    files = [
        ("instagram", "rag/normas_instagram.txt"),
        ("facebook", "rag/normas_facebook.txt"),
        ("linkedin", "rag/normas_linkedin.txt"),
    ]

    for platform, file_path in files:

        content = Path(
            file_path
        ).read_text(
            encoding="utf-8"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "platform": platform
                }
            )
        )

    return documents


def build_vector_store():

    print("Loading documents...")

    documents = load_documents()

    print(
        f"Loaded {len(documents)} documents."
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    print(
        "Creating ChromaDB..."
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    print(
        "Vector database created successfully."
    )


if __name__ == "__main__":

    build_vector_store()