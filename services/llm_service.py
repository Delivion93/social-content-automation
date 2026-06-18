from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0.7
)

def ask(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content