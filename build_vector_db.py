from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings


documents = [

    Document(
        page_content=open(
            "rag/normas_instagram.txt",
            encoding="utf-8"
        ).read(),
        metadata={
            "platform": "instagram"
        }
    ),

    Document(
        page_content=open(
            "rag/normas_facebook.txt",
            encoding="utf-8"
        ).read(),
        metadata={
            "platform": "facebook"
        }
    ),

    Document(
        page_content=open(
            "rag/normas_linkedin.txt",
            encoding="utf-8"
        ).read(),
        metadata={
            "platform": "linkedin"
        }
    )
]

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

Chroma.from_documents(
    documents,
    embeddings,
    persist_directory="vectorstore"
)

