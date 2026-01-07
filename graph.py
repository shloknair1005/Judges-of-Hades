from langgraph.graph import StateGraph
from agents.nidhi_agent import finance_agent
from agents.hades import hades_agent
from agents.karan_agent import sales_agent
from agents.shlok_agent import ops_model

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("sales", sales_agent)
    graph.add_node("ops", ops_model)
    graph.add_node("finance", finance_agent)
    graph.add_node("final_decision", hades_agent)

    graph.set_entry_point("sales")
    graph.add_edge("sales", "ops")
    graph.add_edge("ops", "finance")
    graph.add_edge("finance", "final_decision")
    graph.set_exit_point("final_decision")

    return graph.compile()
