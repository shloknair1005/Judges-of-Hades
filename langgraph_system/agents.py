from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize different LLMs for each agent
sales_llm = ChatGroq(
    temperature=0.8,
    model_name="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

operations_llm = ChatGroq(
    temperature=0.6,
    model_name="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

finance_llm = ChatGroq(
    temperature=0.5,
    model_name="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

hades_llm = ChatGroq(
    temperature=0.7,
    model_name="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

print("\n" + "=" * 70)
print("🤖 LANGGRAPH AGENTS INITIALIZED:")
print("  Sales      → Mixtral 8x7B (Creative & Persuasive)")
print("  Operations → Llama 3 70B (Balanced & Practical)")
print("  Finance    → Gemma 2 9B (Analytical & Precise)")
print("  Hades      → Llama 3.1 70B (Wise & Comprehensive)")
print("=" * 70 + "\n")


# ========== ROUND 1: Initial Positions ==========

def sales_initial_node(state: dict) -> dict:
    """Sales agent gives initial recommendation"""
    print("\n🔵 SALES - Initial Position")

    messages = [
        SystemMessage(content="""You are a passionate Sales Strategist with 15 years of experience.
        You believe revenue growth is the lifeblood of any business.
        You are bold and ambitious in your recommendations."""),
        HumanMessage(content=f"""Analyze this business problem from a SALES perspective:

        Problem: {state['problem']}

        Provide ONE clear, actionable recommendation focused on sales and revenue growth.
        Be specific and practical. (2-3 sentences)""")
    ]

    response = sales_llm.invoke(messages)
    state['sales_initial'] = response.content
    print(f"✓ Sales Initial: {response.content[:100]}...")
    return state


def operations_initial_node(state: dict) -> dict:
    """Operations agent gives initial recommendation"""
    print("\n🟢 OPERATIONS - Initial Position")

    messages = [
        SystemMessage(content="""You are a pragmatic Operations expert who has scaled multiple businesses.
        You focus on execution, resources, and feasibility.
        You are realistic and point out potential failures."""),
        HumanMessage(content=f"""Analyze this business problem from an OPERATIONS perspective:

        Problem: {state['problem']}

        Provide ONE clear, actionable recommendation focused on execution and scalability.
        Be realistic about what can be implemented. (2-3 sentences)""")
    ]

    response = operations_llm.invoke(messages)
    state['operations_initial'] = response.content
    print(f"✓ Operations Initial: {response.content[:100]}...")
    return state


def finance_initial_node(state: dict) -> dict:
    """Finance agent gives initial recommendation"""
    print("\n🟡 FINANCE - Initial Position")

    messages = [
        SystemMessage(content="""You are a cautious CFA and CA with expertise in risk management.
        You focus on ROI, cash flow, and financial sustainability.
        You are conservative but pragmatic."""),
        HumanMessage(content=f"""Analyze this business problem from a FINANCE perspective:

        Problem: {state['problem']}

        Provide ONE clear, actionable recommendation focused on financial health and risk.
        Consider cash flow, ROI, and margins. (2-3 sentences)""")
    ]

    response = finance_llm.invoke(messages)
    state['finance_initial'] = response.content
    print(f"✓ Finance Initial: {response.content[:100]}...")
    return state


# ========== ROUND 2: Debate ==========

def sales_debate_node(state: dict) -> dict:
    """Sales agent challenges other positions"""
    print("\n🔵 SALES - Debate Round")

    messages = [
        SystemMessage(content="""You are a competitive Sales Strategist.
        You will now challenge the Operations and Finance perspectives if you disagree."""),
        HumanMessage(content=f"""You've heard these recommendations:

        Operations said: {state['operations_initial']}
        Finance said: {state['finance_initial']}

        Now CHALLENGE their points if you disagree:
        - If Operations is too cautious, argue why opportunity outweighs risk
        - If Finance is too conservative, argue why the investment will pay off
        - Be assertive but professional

        (3-4 sentences)""")
    ]

    response = sales_llm.invoke(messages)
    state['sales_debate'] = response.content
    print(f"✓ Sales Debate: {response.content[:100]}...")
    return state


def operations_debate_node(state: dict) -> dict:
    """Operations agent challenges other positions"""
    print("\n🟢 OPERATIONS - Debate Round")

    messages = [
        SystemMessage(content="""You are a direct Operations expert.
        You will now challenge the Sales and Finance perspectives if you disagree."""),
        HumanMessage(content=f"""You've heard these recommendations:

        Sales said: {state['sales_initial']}
        Finance said: {state['finance_initial']}

        Now CHALLENGE their points if you disagree:
        - If Sales is unrealistic, explain the operational bottlenecks
        - If Finance is blocking necessary investment, argue why we need resources
        - Provide concrete execution concerns

        (3-4 sentences)""")
    ]

    response = operations_llm.invoke(messages)
    state['operations_debate'] = response.content
    print(f"✓ Operations Debate: {response.content[:100]}...")
    return state


def finance_debate_node(state: dict) -> dict:
    """Finance agent challenges other positions"""
    print("\n🟡 FINANCE - Debate Round")

    messages = [
        SystemMessage(content="""You are a data-driven Financial Strategist.
        You will now challenge the Sales and Operations perspectives if you disagree."""),
        HumanMessage(content=f"""You've heard these recommendations:

        Sales said: {state['sales_initial']}
        Operations said: {state['operations_initial']}

        Now CHALLENGE their points if you disagree:
        - If Sales is proposing risky spending, show the financial danger
        - If Operations wants expensive infrastructure, demand ROI justification
        - Use numbers and risk analysis

        (3-4 sentences)""")
    ]

    response = finance_llm.invoke(messages)
    state['finance_debate'] = response.content
    print(f"✓ Finance Debate: {response.content[:100]}...")
    return state


# ========== ROUND 3: Final Positions ==========

def sales_final_node(state: dict) -> dict:
    """Sales agent gives final position after debate"""
    print("\n🔵 SALES - Final Position")

    messages = [
        SystemMessage(content="""You've debated with Operations and Finance.
        Now provide your final refined recommendation."""),
        HumanMessage(content=f"""After this debate:

        Operations argued: {state['operations_debate']}
        Finance argued: {state['finance_debate']}

        Refine your recommendation:
        - Acknowledge valid points from others
        - Adjust your position if needed, or double down if confident
        - Provide your FINAL recommendation

        (2-3 sentences)""")
    ]

    response = sales_llm.invoke(messages)
    state['sales_final'] = response.content
    print(f"✓ Sales Final: {response.content[:100]}...")
    return state


def operations_final_node(state: dict) -> dict:
    """Operations agent gives final position after debate"""
    print("\n🟢 OPERATIONS - Final Position")

    messages = [
        SystemMessage(content="""You've debated with Sales and Finance.
        Now provide your final refined recommendation."""),
        HumanMessage(content=f"""After this debate:

        Sales argued: {state['sales_debate']}
        Finance argued: {state['finance_debate']}

        Refine your recommendation:
        - Acknowledge valid points from others
        - Adjust if needed, or hold firm if necessary
        - Provide your FINAL recommendation

        (2-3 sentences)""")
    ]

    response = operations_llm.invoke(messages)
    state['operations_final'] = response.content
    print(f"✓ Operations Final: {response.content[:100]}...")
    return state


def finance_final_node(state: dict) -> dict:
    """Finance agent gives final position after debate"""
    print("\n🟡 FINANCE - Final Position")

    messages = [
        SystemMessage(content="""You've debated with Sales and Operations.
        Now provide your final refined recommendation."""),
        HumanMessage(content=f"""After this debate:

        Sales argued: {state['sales_debate']}
        Operations argued: {state['operations_debate']}

        Refine your recommendation:
        - Acknowledge valid points from others
        - Adjust if the ROI case is strong, or maintain caution
        - Provide your FINAL recommendation

        (2-3 sentences)""")
    ]

    response = finance_llm.invoke(messages)
    state['finance_final'] = response.content
    print(f"✓ Finance Final: {response.content[:100]}...")
    return state


# ========== FINAL: Hades Decision ==========

def hades_decision_node(state: dict) -> dict:
    """Hades makes the final decision"""
    print("\n⚫ HADES - Final Decision")

    messages = [
        SystemMessage(content="""You are Hades, the wise judge who has witnessed this entire debate.
        You make the final balanced decision considering all perspectives."""),
        HumanMessage(content=f"""Original Problem: {state['problem']}

        You witnessed:

        ROUND 1 - Initial Positions:
        Sales: {state['sales_initial']}
        Operations: {state['operations_initial']}
        Finance: {state['finance_initial']}

        ROUND 2 - Debate:
        Sales: {state['sales_debate']}
        Operations: {state['operations_debate']}
        Finance: {state['finance_debate']}

        ROUND 3 - Final Positions:
        Sales: {state['sales_final']}
        Operations: {state['operations_final']}
        Finance: {state['finance_final']}

        Now make your FINAL DECISION:
        1. Acknowledge the strongest arguments from each side
        2. Identify which advisor had the most compelling case
        3. Make a balanced decision considering all perspectives
        4. Explain the trade-offs you're accepting
        5. Be decisive and clear

        (4-5 sentences)""")
    ]

    response = hades_llm.invoke(messages)
    state['final_decision'] = response.content
    print(f"✓ Hades Decision: {response.content[:100]}...")
    return state