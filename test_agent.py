from any_agent import AgentConfig, AnyAgent

agent = AnyAgent.create(
    "openai",
    AgentConfig(
        model_id="openai/Qwen3.5-0.8B-Q8_0.gguf",
        instructions="You are a helpful assistant.",
        api_base="http://172.17.112.1:8080/v1",
        api_key="dummy",
    ),
)

result = agent.run("Say hello and tell me your model name.")
print(result.final_output)
