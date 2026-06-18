from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b"
)

response = llm.invoke(
    "Generate a short marketing idea for a coffee shop."
)

print(response.content)