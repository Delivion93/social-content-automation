import os
from langchain_ollama import ChatOllama

OLLAMA_API_BASE_URL = os.getenv(
    "OLLAMA_API_BASE_URL",
    os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
)

llm = ChatOllama(
    model="gemma3:4b",
    #model = "qwen3:8b",
    #model = "qwen3:4b-instruct",
    base_url=OLLAMA_API_BASE_URL,
    temperature=0.7,
    #num_ctx=8192
    
)

def ask(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content