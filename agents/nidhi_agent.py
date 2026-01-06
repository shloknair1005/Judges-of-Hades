from llms.hf_client import call_hf
from config import FINANCE_MODEL


def finance_agent(state:dict) -> dict:
    prompt = f"""
You are a Financial Strategist.
You have a qualification of Chartered Financial Analyst and Chartered Accountant.
You protect cash flow, margins, and risk exposure.
You have good experience at auditing and risk management.

Problem:
{state['problem']}

Give ONE recommendation.
"""
    
    state["finance"] = call_hf(FINANCE_MODEL, prompt)
    return state

