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

    campaign_json = json.dumps(
        campaign,
        indent=2,
        ensure_ascii=False
    )

    def build_edit_instruction(user_message: str) -> str:

        message = user_message.lower()

        if "instagram" in message:
            return """
    Modifica EXCLUSIVAMENTE el campo instagram_post.

    Todos los demás campos deben permanecer EXACTAMENTE iguales.
    """

        if "facebook" in message:
            return """
    Modifica EXCLUSIVAMENTE el campo facebook_post.

    Todos los demás campos deben permanecer EXACTAMENTE iguales.
    """

        if "linkedin" in message:
            return """
    Modifica EXCLUSIVAMENTE el campo linkedin_post.

    Todos los demás campos deben permanecer EXACTAMENTE iguales.
    """

        if "tone" in message or "tono" in message:
            return """
    Modifica el tono.

    Actualiza únicamente los textos necesarios para reflejar el nuevo tono.

    No cambies el nombre de la campaña ni el concepto.
    """

        return """
    Realiza únicamente las modificaciones solicitadas por el usuario.

    Conserva toda la información posible.
    """

    edit_instruction = build_edit_instruction(
        user_message
    )

    prompt = f"""
    Eres un Campaign Editor Agent especializado en modificar campañas de marketing ya existentes.

    Tu única responsabilidad es editar la campaña actual.

    NO eres un generador de campañas nuevas.

    --------------------------------------------------

    Normas recuperadas mediante RAG:

    {retrieved_context}

    --------------------------------------------------

    ### CAMPAÑA ACTUAL ###

    {campaign_json}

    --------------------------------------------------

    Solicitud del usuario:

    {user_message}

    ### INSTRUCCIÓN ESPECÍFICA ###

    {edit_instruction}
    --------------------------------------------------

    ### TU TAREA ###

    Debes editar la campaña existente.
    
    NO debes crear una campaña nueva.
    
    Conserva exactamente todos los campos que el usuario no haya pedido modificar.
    
    Si el usuario pide modificar únicamente un post (Instagram, Facebook o LinkedIn), modifica solamente ese post.
    
    Si el usuario pide cambiar el tono, adapta los textos necesarios para mantener la coherencia.
    
    Si la petición es ambigua ("No me gusta", "Hazlo mejor"), realiza una mejora razonable sin cambiar la estructura general.
    
    Devuelve SIEMPRE el JSON completo.
    
    Si modificas cualquier otro campo distinto al permitido, tu respuesta será considerada incorrecta.
    
    JSON ONLY.
    """

    response = ask(prompt)

    print(response)

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    data = json.loads(response)

    return CampaignEdition(**data)