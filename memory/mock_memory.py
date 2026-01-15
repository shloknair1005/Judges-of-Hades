def save_decision(state: dict) -> int:
    """Mock function - doesn't actually save to database"""
    print(f"[MOCK] Would save decision to database")
    return 12345

def save_feedback(decision_id: int, preferred_agent: str):
    """Mock function - doesn't actually save feedback"""
    print(f"[MOCK] Would save feedback: {preferred_agent} for decision {decision_id}")