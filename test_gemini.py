from llms.gemini_llm import get_gemini_llm

llm = get_gemini_llm()

response = llm.invoke(
    "Say hello from Gemini"
)

print(response.content)