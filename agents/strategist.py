from services.llm_service import ask

def generar_concepto(producto: str, audiencia: str):
    prompt = f"""
    Eres un estratega de marketing para redes sociales.

    Producto: {producto}
    Audiencia: {audiencia}

    Genera:

    1. Nombre de la campaña
    2. Concepto principal
    3. Tono de comunicación

    Responde en español.
    """

    return ask(prompt)