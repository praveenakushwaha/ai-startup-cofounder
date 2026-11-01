from llms.groq_llm import get_groq_llm

llm = get_groq_llm()

response = llm.invoke(
    "Say hello from Groq"
)

print(response.content)