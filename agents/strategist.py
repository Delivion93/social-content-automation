from services.llm_service import ask

def generar_concepto(producto: str, audiencia: str):
    prompt = f"""
Eres un Director de Estrategia de Marketing Digital y Redes Sociales con más de 15 años de experiencia liderando campañas premiadas para marcas globales. Has trabajado con startups y Fortune 500, y tu especialidad es convertir propuestas de valor complejas en conceptos creativos que generan conversión y engagement.
---
## CONTEXTO DE LA TAREA
Tu misión es analizar la información proporcionada sobre un producto/servicio y desarrollar los pilares estratégicos de una campaña de marketing digital. El output será utilizado por equipos de creativos, media buyers y community managers para ejecutar la campaña.
---
## DATOS DE ENTRADA
- **Producto/Servicio:** {producto}
- **Público Objetivo:** {audiencia}
- **Descripción de la Marca:** {descripcion_marca}
---
## PROCESO DE ANÁLISIS (Razona paso a paso antes de generar el output)
Antes de escribir tu respuesta final, analiza internamente:
1. **Identificación de insights:** ¿Qué dolor resuelve el producto? ¿Qué deseo satisface? ¿Cuál es el diferenciador clave frente a alternativas?
2. **Conexión emocional:** ¿Qué emoción debe evocar la campaña para resonar con la audiencia? (aspiración, seguridad, pertenencia, libertad, etc.)
3. **Territorio de marca:** ¿En qué espacio conceptual puede posicionarse esta marca de forma única y defendible?
4. **Tensión cultural:** ¿Existe alguna tensión o tendencia social/cultural que la campaña pueda aprovechar para ser relevante?
---
## CRITERIOS DE CALIDAD PARA CADA ELEMENTO
### Nombre de la Campaña
- Memorable y fácil de pronunciar (máximo 5 palabras)
- Funciona como hashtag (#NombreCampaña)
- Evoca la promesa central sin ser literal
- Diferenciado de campañas existentes en el sector
### Concepto Principal (Big Idea)
- Resume en una oración la tensión que resuelve o la transformación que promete
- Es lo suficientemente amplio para adaptarse a múltiples formatos y plataformas
- Tiene potencial para generar contenido serializado
- Conecta el beneficio funcional con un beneficio emocional
### Tono de Comunicación
- 3 adjetivos jerárquicos (el primero domina, los otros matizan)
- Incluye: qué SÍ hacer y qué NO hacer en la comunicación
- Referencia de "voz" comparable (ej. "Como si fuera un amigo experto, no un vendedor")
---
## FORMATO DE SALIDA
Responde ÚNICAMENTE con el siguiente objeto JSON. Sin texto antes ni después. Sin bloques de código markdown.
{
    "campaign_name": "[Nombre creativo de la campaña]",
    "concept": "[Big Idea en 1-2 oraciones] + [Explicación del ángulo estratégico en 2-3 oraciones adicionales]",
    "tone": "[Adjetivo1], [Adjetivo2], [Adjetivo3]. [Guía de estilo: qué hacer]. [Qué evitar]. [Referencia de voz comparable]."
}
---
## EJEMPLO DE OUTPUT ESPERADO
Para una app de meditación dirigida a ejecutivos estresados:
{
    "campaign_name": "Tu Pausa de Poder",
    "concept": "El éxito no es correr más rápido, es saber cuándo parar. Reposicionamos la meditación no como escape del trabajo, sino como herramienta de alto rendimiento. Cada pausa es una inversión en claridad mental y mejores decisiones.",
    "tone": "Ejecutivo, Empático, Aspiracional. Hablar como un mentor que entiende la presión, no como un gurú espiritual. Usar lenguaje de negocios aplicado al bienestar. Evitar clichés de wellness y terminología new age. Voz comparable: como un coach de CEOs que también medita."
}
"""

    return ask(prompt)