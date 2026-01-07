from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY   

client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_decision(state: dict) -> int:
    res = client.table("decisions").insert({
        "problem": state["problem"],
        "sales": state["sales"],
        "operations": state["operations"],
        "finance": state["finance"],
        "final_decision": state["final_decision"]
    }).execute()

    return res.data[0]["id"]

def save_feedback(decision_id: int, preferred_agent: str):
    res = client.table("decision") \
        .update({"preferred_agent": preferred_agent}) \
        .eq("id", decision_id) \
        .execute()
