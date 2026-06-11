import os
os.environ["OPENAI_API_KEY"] = "dummy"
os.environ["OPENAI_API_BASE"] = "http://172.17.112.1:8080/v1"
import requests
from any_agent import AnyAgent, AgentConfig

ENCODER_URL = "http://localhost:8080"
LLM_URL = "http://172.17.112.1:8080/v1"

DOC_PATH = "docs/sample_policy.txt"


def retrieve_context(query):
    with open(DOC_PATH, "r") as f:
        text = f.read()

    chunks = [text[i:i+300] for i in range(0, len(text), 300)]

    resp = requests.post(
        f"{ENCODER_URL}/predict",
        json={"inputs": [query] + chunks}
    )

    results = resp.json()["results"]

    query_emb = results[0]["embedding"]

    best_chunk = chunks[0]

    return best_chunk


agent = AnyAgent.create(
    "openai",
    AgentConfig(
        model_id="openai/Qwen3.5-0.8B-Q8_0.gguf",
        api_base=LLM_URL,
        instructions="""
You are a RAG assistant.
Answer ONLY using the provided context.
"""
    )
)

while True:
    q = input("\nQuestion: ")

    if q.lower() == "quit":
        break

    context = retrieve_context(q)

    prompt = f"""
Context:
{context}

Question:
{q}
"""

    trace = agent.run(prompt)

    print("\nAnswer:\n")
    print(trace.final_output)
