import subprocess
import sys

subprocess.run(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "frontend/streamlit_ui.py"
    ]
)