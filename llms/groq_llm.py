import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_groq_llm():

    return ChatGroq(
    # model="llama-3.1-8b-instant",
        model="qwen/qwen3.8-27b",
        temperature=0.3,
        max_tokens=50
    )