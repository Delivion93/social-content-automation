import anthropic
import json

client = anthropic.Anthropic(api_key="sk-ant-...")

def copywriter_agent(concepto: str, tono: str) -> dict:
    """
    Copywriter Agent — genera copys adaptados para Instagram, Facebook y LinkedIn.

    Entrada:
        concepto (str): El concepto de la campaña.
        tono (str): El tono de comunicación (ej: "profesional y cercano").

    Salida:
        dict con keys: "instagram", "facebook", "linkedin"
    """

    prompt = f"""Eres un copywriter experto en redes sociales.
Concepto de campaña: "{concepto}"
Tono de comunicación: {tono}

Genera copys adaptados para cada plataforma respetando sus características:
- Instagram: máximo 150 caracteres + 5 hashtags relevantes. Emojis permitidos.
- Facebook: 150-300 caracteres, tono conversacional, una pregunta al final para generar engagement.
- LinkedIn: 200-400 caracteres, tono profesional, datos o insight si aplica, sin emojis excesivos.

Responde SOLO con un JSON válido, sin texto extra ni backticks. Formato exacto:
{{"instagram":"...","facebook":"...","linkedin":"..."}}"""

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    texto = response.content[0].text.strip()
    copys = json.loads(texto)
    return copys


def mostrar_resultados(copys: dict):
    print("\n" + "="*50)
    print("📸 INSTAGRAM")
    print("="*50)
    print(copys["instagram"])
    print(f"({len(copys['instagram'])} caracteres)")

    print("\n" + "="*50)
    print("📘 FACEBOOK")
    print("="*50)
    print(copys["facebook"])
    print(f"({len(copys['facebook'])} caracteres)")

    print("\n" + "="*50)
    print("💼 LINKEDIN")
    print("="*50)
    print(copys["linkedin"])
    print(f"({len(copys['linkedin'])} caracteres)")
    print()


if __name__ == "__main__":
    concepto = "Lanzamos una app de meditación para profesionales con poco tiempo"
    tono = "inspirador y motivacional"

    print(f"Generando copys para: '{concepto}'")
    print(f"Tono: {tono}\n")

    copys = copywriter_agent(concepto, tono)
    mostrar_resultados(copys)