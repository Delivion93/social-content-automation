from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from graph.content_graph import graph
from validators.brands import KNOWN_BRANDS
from schemas.chat import ChatRequest
from agents.editor_agent import edit_campaign
from agents.reception_agent import detect_user_intent


class GenerateRequest(BaseModel):
    product: str
    audience: str
    brand_description: str


app = FastAPI()
current_campaign = {}
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="landing.html"
    )


@app.get("/generate", response_class=HTMLResponse)
async def generate_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="generate.html"
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

    reception = detect_user_intent(
        request.message
    )

    if reception.intent == "GENERAL":

        return {
            "status": "GENERAL",
            "message": reception.message
        }

    edited_campaign = edit_campaign(
        campaign=current_campaign,
        user_message=request.message
    )

    current_campaign.update(
        edited_campaign.model_dump()
    )

    return {
        "status": "EDIT",
        "message": reception.message,
        "campaign": current_campaign
    }