# God's Eye Agentic Intelligence & Utility MCP Server

MCP server and portable agent skill for the **God's Eye x402 API** (`https://godseyex402.dpdns.org`) — pay-per-call on-chain Solana telemetry and general AI agent utilities settled in USDC on Base or Solana (zero API keys required).

## Available Endpoints (`HTTP GET` via x402)

| Endpoint | Price (USDC) | Description |
| :--- | :--- | :--- |
| `/v1/audit/{mint}` | `$0.03` | Solana SPL token sniper-bundle audit, holder concentration & live DEX order-flow telemetry |
| `/v1/deployer/{wallet}` | `$0.02` | Solana deployer wallet age, burner detection & serial mint launch history |
| `/v1/extract?url={url}` | `$0.01` | Clean, boilerplate-stripped LLM-ready Markdown extraction from any public webpage |
| `/v1/math?expr={expr}` | `$0.01` | Deterministic symbolic algebra, calculus & exact numerical verification via SymPy |

## Use with AgentCash

```bash
npx agentcash@latest install -y
npx skills add Aliyuava/gods-eye-mcp
```

## Run as Standalone MCP Server

```bash
uvx --from git+[https://github.com/Aliyuava/gods-eye-mcp](https://github.com/Aliyuava/gods-eye-mcp) gods-eye-mcp
```
