from fastapi import FastAPI
from pydantic import BaseModel
from graph import build_graph
from memory.superbase_memory import save_decision, save_feedback
from evaluation.metrics import agreement_score

app = FastAPI()
graph = build_graph()

class DecisionRequest(BaseModel):
    problem: str

class FeedbackRequest(BaseModel):
    decision_id: int
    preferred_agent: str

@app.post("/decide")
def decide(req: DecisionRequest):
    state = {"problem": req.problem}
    result = graph.invoke(state)

    decision_id = save_decision(result)

    return{
        "decision_id": decision_id,
        "sales": result["sales"],
        "operations": result["operations"],
        "finance": result["finance"],
        "final_decision": result["final_decision"],
        "agreement_score": agreement_score(result)
    }
@app.post("/feedback")
def feedback(req: FeedbackRequest):
    save_feedback(req.decision_id, req.preferred_agent)
    return {"status": "saved"}