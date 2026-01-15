from langgraph.graph import StateGraph, END
from langgraph_system.state import JudgesState
from langgraph_system.agents import (
    sales_initial_node, operations_initial_node, finance_initial_node,
    sales_debate_node, operations_debate_node, finance_debate_node,
    sales_final_node, operations_final_node, finance_final_node,
    hades_decision_node
)


def build_judges_graph():
    """Build the LangGraph workflow"""

    # Create graph
    workflow = StateGraph(JudgesState)

    # Add Round 1 nodes
    workflow.add_node("sales_initial", sales_initial_node)
    workflow.add_node("operations_initial", operations_initial_node)
    workflow.add_node("finance_initial", finance_initial_node)

    # Add Round 2 nodes
    workflow.add_node("sales_debate", sales_debate_node)
    workflow.add_node("operations_debate", operations_debate_node)
    workflow.add_node("finance_debate", finance_debate_node)

    # Add Round 3 nodes
    workflow.add_node("sales_final", sales_final_node)
    workflow.add_node("operations_final", operations_final_node)
    workflow.add_node("finance_final", finance_final_node)

    # Add Hades node
    workflow.add_node("hades_decision", hades_decision_node)

    # Define the flow
    workflow.set_entry_point("sales_initial")

    # Round 1 flow
    workflow.add_edge("sales_initial", "operations_initial")
    workflow.add_edge("operations_initial", "finance_initial")

    # Move to Round 2
    workflow.add_edge("finance_initial", "sales_debate")

    # Round 2 flow
    workflow.add_edge("sales_debate", "operations_debate")
    workflow.add_edge("operations_debate", "finance_debate")

    # Move to Round 3
    workflow.add_edge("finance_debate", "sales_final")

    # Round 3 flow
    workflow.add_edge("sales_final", "operations_final")
    workflow.add_edge("operations_final", "finance_final")

    # Final decision
    workflow.add_edge("finance_final", "hades_decision")
    workflow.add_edge("hades_decision", END)

    return workflow.compile()