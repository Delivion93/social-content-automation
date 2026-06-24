from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import HTTPException
from graph.content_graph import graph
from validators.brands import KNOWN_BRANDS
from schemas.chat import ChatRequest
from agents.editor_agent import edit_campaign


class GenerateRequest(BaseModel):
    product: str
    audience: str
    brand_description: str


app = FastAPI()
current_campaign = {}

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

    global current_campaign

    result = graph.invoke(
        {
            "product": data.product,
            "audience": data.audience,
            "brand_description": data.brand_description,
            "revision_count": 0
        }
    )

    current_campaign = result

    return result
@app.post("/chat")
async def chat(request: ChatRequest):

    global current_campaign

    edited_campaign = edit_campaign(
        campaign=current_campaign,
        user_message=request.message
    )

    current_campaign.update(
        edited_campaign.model_dump()
    )

    return {
        "campaign": current_campaign
    }