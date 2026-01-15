from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from schemas import DecisionRequest, DecisionResponse, FeedbackRequest
from langgraph_system.graph import build_judges_graph
from memory.mock_memory import save_decision, save_feedback

app = FastAPI(title="Judges of Hades - LangGraph + Groq")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build graph once at startup
graph = build_judges_graph()


@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/decide", response_model=DecisionResponse)
def decide(req: DecisionRequest):
    try:
        print("\n" + "=" * 70)
        print("⚔️  JUDGES OF HADES - LANGGRAPH DEBATE SESSION")
        print(f"Problem: {req.problem}")
        print("=" * 70)

        # Run the graph
        result = graph.invoke({
            "problem": req.problem,
            "sales_initial": "",
            "operations_initial": "",
            "finance_initial": "",
            "sales_debate": "",
            "operations_debate": "",
            "finance_debate": "",
            "sales_final": "",
            "operations_final": "",
            "finance_final": "",
            "final_decision": ""
        })

        print("\n" + "=" * 70)
        print("✅ DEBATE COMPLETE")
        print("=" * 70 + "\n")

        decision_id = save_decision(result)

        return DecisionResponse(
            decision_id=str(decision_id),
            final_decision=result["final_decision"],
            agents={
                "sales": f"""ROUND 1: {result['sales_initial']}

DEBATE: {result['sales_debate']}

FINAL: {result['sales_final']}""",
                "operations": f"""ROUND 1: {result['operations_initial']}

DEBATE: {result['operations_debate']}

FINAL: {result['operations_final']}""",
                "finance": f"""ROUND 1: {result['finance_initial']}

DEBATE: {result['finance_debate']}

FINAL: {result['finance_final']}"""
            }
        )

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/feedback")
def feedback(req: FeedbackRequest):
    save_feedback(req.decision_id, req.chosen_agent)
    return {"status": "saved"}


