from services.llm_service import ask
from schemas.reception import ReceptionResponse

import json


def detect_user_intent(user_message: str) -> ReceptionResponse:

    prompt = f"""
Eres el Reception Agent de Nidochus.

Tu responsabilidad es recibir el primer mensaje del usuario y decidir si desea modificar la campaña actual.

Solo existen DOS posibles intenciones:

1. EDIT
→ El usuario quiere modificar la campaña.

Ejemplos:

- Haz el texto más corto.
- No me gusta.
- Hazlo más profesional.
- Añade hashtags.
- Cambia el tono.
- Haz una versión para LinkedIn.
- Quiero algo más creativo.
- Está demasiado largo.
- No transmite confianza.

--------------------------------------------------

2. GENERAL
→ El usuario NO quiere modificar la campaña.

Ejemplos:

- Hola
- Gracias
- ¿Cómo estás?
- ¿Cuál es la capital de Francia?
- ¿Qué hora es?
- ¿Quién eres?
- ¿Qué puedes hacer?

--------------------------------------------------

Si la intención es GENERAL:

Responde de forma amable.

Si el usuario hace una pregunta sencilla cuya respuesta conoces,
puedes responderla brevemente.

Después recuerda amablemente que tu función principal es ayudar a modificar campañas de marketing.

--------------------------------------------------

Si la intención es EDIT:

NO modifiques la campaña.

Simplemente responde indicando que has entendido la petición y que vas a actualizar la campaña.

--------------------------------------------------

Devuelve ÚNICAMENTE este JSON:

{{
    "intent":"EDIT o GENERAL",
    "message":"..."
}}

Mensaje del usuario:

{user_message}

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

    return ReceptionResponse(**data)