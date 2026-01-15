from pydantic import BaseModel
from typing import Dict

class DecisionRequest(BaseModel):
    problem: str

class DecisionResponse(BaseModel):
    decision_id: str
    final_decision: str
    agents: Dict[str, str]

class FeedbackRequest(BaseModel):
    decision_id: str
    chosen_agent: str
