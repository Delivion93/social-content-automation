from langgraph.graph import StateGraph, START, END

from graph.state import ContentState

# Тимчасові заглушки
from agents.strategist_agent import strategist_node
from agents.copywriter_agent import copywriter_node
from agents.compliance_agent import compliance_node

builder = StateGraph(ContentState)

# Nodes
builder.add_node("strategist", strategist_node)
builder.add_node("copywriter", copywriter_node)
builder.add_node("compliance", compliance_node)

# Flow
builder.add_edge(START, "strategist")
builder.add_edge("strategist", "copywriter")
builder.add_edge("copywriter", "compliance")
builder.add_edge("compliance", END)

graph = builder.compile()