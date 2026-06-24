import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from graph.content_graph import should_retry_copywriter

state = {"approved": True, "revision_count": 0}
print(should_retry_copywriter(state))