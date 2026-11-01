from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import StartupState

from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent
from agents.cto_agent import cto_agent
from agents.finance_agent import finance_agent
from agents.final_report_agent import final_report_agent
from agents.risk_agent import risk_agent
from agents.scoring_agent import scoring_agent
from agents.investor_agent import investor_agent
from agents.supervisor_agent import supervisor_agent


def build_graph():

    workflow = StateGraph(StartupState)

    workflow.add_node(
        "market_agent",
        market_agent
    )

    workflow.add_node(
        "competitor_agent",
        competitor_agent
    )

    workflow.add_node(
        "cto_agent",
        cto_agent
    )

    workflow.add_node(
        "finance_agent",
        finance_agent
    )
    workflow.add_node(
        "risk_agent",
        risk_agent
    )

    workflow.add_node(
    "scoring_agent",
    scoring_agent
    )

    workflow.add_node(
    "investor_agent",
    investor_agent
    )

    workflow.add_node(
    "final_report_agent",
    final_report_agent
    )

    workflow.add_node(
    "supervisor_agent",
    supervisor_agent
    )

    # $$$$$$$$$$$

    workflow.set_entry_point(
        "supervisor_agent"
    )

    workflow.add_edge(
    "supervisor_agent",
    "market_agent"
    )

    workflow.add_edge(
        "market_agent",
        "competitor_agent"
    )

    workflow.add_edge(
        "competitor_agent",
        "cto_agent"
    )

    workflow.add_edge(
        "cto_agent",
        "finance_agent"
    )

    workflow.add_edge(
        "finance_agent",
        "risk_agent"
    )

    workflow.add_edge(
        "risk_agent",
        "investor_agent"       
    )

    workflow.add_edge(
        "investor_agent",
        "scoring_agent"
    )

    workflow.add_edge(
        "scoring_agent",
        "final_report_agent"
    )

    workflow.add_edge(
        "final_report_agent",
        END
    )

    return workflow.compile()