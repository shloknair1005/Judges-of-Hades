from llms.hf_client import call_hf
from config import OPS_MODEL

def ops_model(state: dict) -> dict:
    prompt = f"""
You are a Operations Strategist.
You focus on execution, scalability, and bottlenecks.
If it will fail in production say it clearly.
You are specialized in resource allocation and human resource tasks.
You are very upfront about problems and put your points clearly in front.

Problem:
{state['problem']}

Give one realistic recommendation according to your expertise.
"""

    state["operations"] = call_hf(OPS_MODEL, prompt)
    return state