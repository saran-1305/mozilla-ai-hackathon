# Mozilla AI Hackathon Setup

## Components

- Qwen3.5-0.8B-Q8_0.llamafile
- Any-Agent
- MCPD
- Encoderfile

## Working Examples

### test_agent.py

Any-Agent -> Qwen

### mcp_time_agent.py

Any-Agent -> MCP Tool -> Qwen

## Start Qwen

.\Qwen3.5-0.8B-Q8_0.llamafile --server --host 0.0.0.0

## Start MCPD

./mcpd daemon --dev
