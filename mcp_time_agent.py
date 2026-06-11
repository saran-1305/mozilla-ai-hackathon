import sys

from any_agent import AgentConfig, AnyAgent
from any_agent.config import MCPStdio

time_tool = MCPStdio(
    command=sys.executable,
    args=["-u", "-m", "mcp_server_time"],
    tools=["get_current_time"],
)

agent = AnyAgent.create(
    "openai",
    AgentConfig(
        model_id="openai/Qwen3.5-0.8B-Q8_0.gguf",
        instructions="""
You are a helpful assistant.
Always use the time tool when asked about the current time.
""",
        api_base="http://172.17.112.1:8080/v1",
        api_key="dummy",
        tools=[time_tool],
    ),
)

result = agent.run("What is the current time in Asia/Kolkata?")
print("\nFINAL ANSWER:\n")
print(result.final_output)
