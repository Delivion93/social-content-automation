from pydantic import BaseModel


class GenerateRequest(BaseModel):
    product: str
    audience: str
    brand_description: str