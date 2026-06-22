from services.llm_service import ask
from schemas.copywriter import CopywriterOutput

import json

def copywriter_node(state):
    """
    LangGraph node.

    Lee la información generada por el Strategist Agent
    y añade las publicaciones al ContentState.
    """
    result = generar_copys(
        concepto=state["concept"],
        tono=state["tone"]
    )

    return {
        "instagram_post": result.instagram_post,
        "facebook_post": result.facebook_post,
        "linkedin_post": result.linkedin_post
    }

def generar_copys(
    concepto: str,
    tono: str
) -> CopywriterOutput:

    prompt = f"""
Eres el Copywriter Agent dentro de un sistema multi-agente basado en LangGraph.

Concepto de campaña:
{concepto}

Tono de comunicación:
{tono}

Tu tarea es crear publicaciones adaptadas para cada plataforma.

Instagram:
- máximo 150 caracteres
- emojis permitidos
- incluir hasta 5 hashtags relevantes

Facebook:
- entre 150 y 300 caracteres
- tono conversacional
- terminar con una pregunta para fomentar interacción

LinkedIn:
- entre 200 y 400 caracteres
- tono profesional
- aportar una reflexión o insight relevante
- evitar exceso de emojis

Responde ÚNICAMENTE con este JSON válido:

{{
    "instagram_post": "...",
    "facebook_post": "...",
    "linkedin_post": "..."
}}
"""

    response = ask(prompt)

    try:
        data = json.loads(response)
        return CopywriterOutput(**data)

    except Exception as e:
        raise ValueError(
            f"Error parsing LLM response: {response}"
        ) from e