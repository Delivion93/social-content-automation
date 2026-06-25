from services.llm_service import ask
from schemas.editor import CampaignEdition

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

import os
import json

OLLAMA_API_BASE_URL = os.getenv(
    "OLLAMA_API_BASE_URL",
    os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
)

def edit_campaign(
    campaign: dict,
    user_message: str
    ) -> CampaignEdition:

    vector_db = Chroma(
        persist_directory="vectorstore",
        embedding_function=OllamaEmbeddings(
            model="nomic-embed-text",
            base_url=OLLAMA_API_BASE_URL
        )
    )

    docs = vector_db.similarity_search(
        user_message,
        k=5
    )

    retrieved_context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    Eres un Campaign Editor Agent.

    NO eres un asistente general.

    Tu única función es modificar campañas.

    Normas recuperadas mediante RAG:

    {retrieved_context}

    Campaña actual:

    {campaign}

    Solicitud:

    {user_message}

    Devuelve la campaña completa.

    JSON ONLY.
    """

    response = ask(prompt)

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    data = json.loads(response)

    return CampaignEdition(**data)