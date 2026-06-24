from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:4b",
    #model = "qwen3:8b",
    #model = "qwen3:4b-instruct",

    temperature=0.7,
    #num_ctx=8192
    
)

def ask(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content