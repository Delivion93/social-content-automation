from agents.strategist_agent import generar_concepto

result = generar_concepto(
    producto="Cafetería de especialidad",
    audiencia="Estudiantes universitarios",
    descripcion_marca="Café moderno con ambiente de estudio y networking"
)

print(result)
print(result.model_dump()) 