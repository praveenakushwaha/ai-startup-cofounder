from graph.workflow import build_graph

graph = build_graph()

state = {
    "startup_idea": "AI Recruitment SaaS",
    # "market_analysis": "",
    # "competitor_analysis": "",
    # "tech_architecture": "",
    # "finance_analysis": "",
    # "risk_analysis": "",
    # "investor_analysis": "",
    "startup_score": "",
    "final_report": ""
    
}

result = graph.invoke(state)

print("\n")
print("=" * 80)
print("FINAL RESULT")
print("=" * 80)

print("\nSTARTUP IDEA")
print("-" * 40)
print(result["startup_idea"])

# print("\nMARKET ANALYSIS")
# print("-" * 40)
# print(result["market_analysis"])

# print("\nCOMPETITOR ANALYSIS")
# print("-" * 40)
# print(result["competitor_analysis"])

# print("\nTECH ARCHITECTURE")
# print("-" * 40)
# print(result["tech_architecture"])

# print("\nFINANCE ANALYSIS")
# print("-" * 40)
# print(result["finance_analysis"])

print("\nFINAL REPORT")
print("=" * 80)

print(result["final_report"])
print("\nSCORES")
print("="*40)

print(
    result.get(
        "scores",
        {}
    )
)