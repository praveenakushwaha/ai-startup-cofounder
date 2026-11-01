import streamlit as st
import time
import json
import os

from datetime import datetime

from graph.workflow import build_graph

from tools.pdf_generator import generate_pdf
from tools.excel_export import export_to_excel
from tools.chart_generator import create_score_chart


REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

# --------------------
# SESSION STATE
# --------------------

if "result" not in st.session_state:
    st.session_state.result = None

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

if "excel_path" not in st.session_state:
    st.session_state.excel_path = None

if "execution_time" not in st.session_state:
    st.session_state.execution_time = 0

# --------------------
# PAGE CONFIG
# --------------------

st.set_page_config(
    page_title="AI Startup Co-Founder",
    page_icon="🚀",
    layout="wide"
)

# --------------------
# SIDEBAR
# --------------------

with st.sidebar:

    st.title("🚀 AI Startup Co-Founder")

    st.subheader("Connected APIs")

    st.success("✅ Groq")
    st.success("✅ Gemini")
    st.success("✅ Google Trends")
    st.success("✅ DuckDuckGo")
    st.success("✅ GitHub")
    st.success("✅ News API")

    st.markdown("---")

    reports = len(os.listdir(REPORTS_DIR))

    st.metric(
        "Reports Generated",
        reports
    )

    if st.session_state.result:

        scores = st.session_state.result.get(
            "scores",
            {}
        )

        st.metric(
            "Overall Score",
            scores.get(
                "overall_score",
                0
            )
        )

# --------------------
# MAIN UI
# --------------------

st.title("🚀 AI Startup Co-Founder")

startup_idea = st.text_input(
    "Enter Startup Idea"
)

if st.button("Generate Report"):

    start_time = time.time()

    graph = build_graph()

    state = {

        "startup_idea": startup_idea,

        "supervisor_decision": "",

        "market_analysis": "",

        "competitor_analysis": "",

        "tech_architecture": "",

        "finance_analysis": "",

        "risk_analysis": "",

        "startup_score": "",

        "scores": {},

        "investor_analysis": "",

        "final_report": ""
    }

    with st.spinner(
        "Running AI Board Meeting..."
    ):

        result = graph.invoke(state)

    create_score_chart(
        result["scores"]
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    pdf_path = os.path.join(
        REPORTS_DIR,
        f"report_{timestamp}.pdf"
    )

    excel_path = os.path.join(
        REPORTS_DIR,
        f"report_{timestamp}.xlsx"
    )

    json_path = os.path.join(
        REPORTS_DIR,
        f"report_{timestamp}.json"
    )

    generate_pdf(
        result,
        pdf_path
    )

    export_to_excel(
        result,
        excel_path
    )

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False,
            default=str
        )

    st.session_state.result = result

    st.session_state.pdf_path = pdf_path

    st.session_state.excel_path = excel_path

    st.session_state.execution_time = round(
        time.time() - start_time,
        2
    )

# --------------------
# DISPLAY RESULTS
# --------------------

if st.session_state.result:

    result = st.session_state.result

    st.success(
        f"Completed in {st.session_state.execution_time} sec"
    )

    st.subheader("🧠 Supervisor Decision")
    st.write(result["supervisor_decision"])

    st.subheader("📈 Market Analysis")
    st.write(result["market_analysis"])

    st.subheader("🎯 Competitor Analysis")
    st.write(result["competitor_analysis"])

    st.subheader("💻 Tech Architecture")
    st.write(result["tech_architecture"])

    st.subheader("💰 Finance Analysis")
    st.write(result["finance_analysis"])

    st.subheader("⚠️ Risk Analysis")
    st.write(result["risk_analysis"])

    st.subheader("📊 Startup Score")
    st.json(result["scores"])

    st.subheader("📊 Score Chart")
    st.image(
        "reports/startup_chart.png"
    )

    st.subheader("💼 Investor Decision")
    st.write(result["investor_analysis"])

    st.subheader("📝 Final Report")
    st.write(result["final_report"])

    st.download_button(
        "📥 Download TXT",
        data=result["final_report"],
        file_name="startup_report.txt"
    )

    with open(
        st.session_state.pdf_path,
        "rb"
    ) as f:

        st.download_button(
            "📄 Download PDF",
            data=f.read(),
            file_name="startup_report.pdf",
            mime="application/pdf"
        )

    with open(
        st.session_state.excel_path,
        "rb"
    ) as f:

        st.download_button(
            "📊 Download Excel",
            data=f.read(),
            file_name="startup_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )