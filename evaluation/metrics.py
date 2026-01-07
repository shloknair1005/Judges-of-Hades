def agreement_score(state: dict) -> float:
    matches = sum([
        state["final_decision"] in state["sales"],
        state["final_decision"] in state["operations"],
        state["final_decision"] in state["finance"]
    ])


    return matches / 3.0
