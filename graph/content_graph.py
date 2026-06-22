from langgraph.graph import StateGraph, START, END

from graph.state import ContentState

# Тимчасові заглушки
from agents.strategist_agent import strategist_node
from agents.compliance_agent import compliance_node


def mock_copywriter_node(state: ContentState):
    return {
        "instagram_post": "Mock Instagram Post",
        "facebook_post": "Mock Facebook Post",
        "linkedin_post": "Mock LinkedIn Post"
    }


builder = StateGraph(ContentState)

# Nodes
builder.add_node("strategist", strategist_node)
builder.add_node("copywriter", mock_copywriter_node)
builder.add_node("compliance", compliance_node)

# Flow
builder.add_edge(START, "strategist")
builder.add_edge("strategist", "copywriter")
builder.add_edge("copywriter", "compliance")
builder.add_edge("compliance", END)

graph = builder.compile()