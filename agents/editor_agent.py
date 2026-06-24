from services.llm_service import ask
from schemas.editor import CampaignEdition
from services.rag_service import load_rules
import json

def edit_campaign(
    campaign: dict,
    user_message: str
    ) -> CampaignEdition:

    rules = load_rules()

    prompt = f"""
    Eres un Campaign Editor Agent.

    NO eres un asistente general.

    Tu única función es modificar campañas.

    Debes respetar siempre las siguientes normas.

    INSTAGRAM:

    {rules["instagram"]}

    FACEBOOK:

    {rules["facebook"]}

    LINKEDIN:

    {rules["linkedin"]}

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