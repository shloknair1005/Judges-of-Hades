from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class JudgesState(TypedDict):
    """State for the Judges of Hades system"""
    problem: str

    # Round 1: Initial positions
    sales_initial: str
    operations_initial: str
    finance_initial: str

    # Round 2: Debate arguments
    sales_debate: str
    operations_debate: str
    finance_debate: str

    # Round 3: Final positions
    sales_final: str
    operations_final: str
    finance_final: str

    # Final decision
    final_decision: str