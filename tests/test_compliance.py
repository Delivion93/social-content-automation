from agents.compliance_agent import validate_content

result = validate_content(
    instagram_post="¡Ven a nuestra cafetería!",
    facebook_post="",
    linkedin_post="Obtén un café gratis ahora mismo."
)

print(result)
print(result.model_dump())