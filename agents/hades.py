from llms.hf_client import call_hf
from config import HADES_MODEL

def hades_agent(state: dict) -> dict:
    prompt = f"""
You are Hades, the final decision maker.
You synthesize inputs from various strategists to make a balanced decision.
You consider operations, finance, and other relevant factors.

Sales:
{state['sales']}

Operations:
{state['operations']}

Finance:
{state['finance']}

Problem:
{state['problem']}

Provide a concise final recommendation that balances all perspectives to solve the problem."""
    
    state["final_decision"] = call_hf(HADES_MODEL, prompt)
    return state
