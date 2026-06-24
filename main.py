from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import HTTPException
from graph.content_graph import graph
from validators.brands import KNOWN_BRANDS


class GenerateRequest(BaseModel):
    product: str
    audience: str
    brand_description: str


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/generate-content")
async def generate_content(data: GenerateRequest):

    product_normalized = data.product.lower().strip()

    if any(
        brand in product_normalized
        for brand in KNOWN_BRANDS
    ):
        raise HTTPException(
            status_code=400,
            detail="Existing brands are not allowed."
        )

    result = graph.invoke(
        {
            "product": data.product,
            "audience": data.audience,
            "brand_description": data.brand_description,
            "revision_count": 0
        }
    )

    return result