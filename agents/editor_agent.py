from services.llm_service import ask
from schemas.editor import CampaignEdition
import json

def edit_campaign(
    campaign: dict,
    user_message: str
    ) -> CampaignEdition:


    prompt = f"""
    Eres un Campaign Editor Agent.

    NO eres un asistente general.

    Tu única función es modificar campañas
    de marketing existentes.

    Campaña actual:

    {campaign}

    Solicitud del usuario:

    {user_message}

    Devuelve SIEMPRE una campaña completa.

    Responde ÚNICAMENTE con JSON válido.

    Formato:

    {{
      "campaign_name": "...",
      "concept": "...",
      "tone": "...",
      "instagram_post": "...",
      "facebook_post": "...",
      "linkedin_post": "..."
    }}
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