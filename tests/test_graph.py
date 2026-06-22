from graph.content_graph import graph

result = graph.invoke(
    {
        "product": "Coffee Shop",
        "audience": "Students",
        "brand_description": "Modern coffee shop for studying",
        "revision_count": 0
    }
)

print(result)