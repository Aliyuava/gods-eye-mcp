---
name: gods-eye-solana-audit
description: Audit Solana SPL tokens for mint/freeze authority traps, Top-9 holder bundle concentration, 5-minute DEX liquidity telemetry, and deployer wallet rug risk via the God's Eye x402 API. Use when evaluating Solana memecoins, verifying contract safety, or checking deployer wallet history before trading.
license: MIT
---

# God's Eye Solana Token & Deployer Telemetry

Paid x402 intelligence endpoints hosted at `https://godseyex402.dpdns.org`. Never guess or modify endpoint paths.

## Endpoints & Fixed USDC Pricing (Base or Solana)

| Purpose | Method & Path | Cost (USDC) |
| :--- | :--- | :--- |
| Token mint, Top-9 bundle & 5m DEX telemetry | `GET https://godseyex402.dpdns.org/v1/audit/{mint}` | `$0.03` |
| Deployer wallet age, burner check & tx history | `GET https://godseyex402.dpdns.org/v1/deployer/{wallet}` | `$0.02` |
| Full OpenAPI 3.1 contract (free) | `GET https://godseyex402.dpdns.org/openapi.json` | `$0.00` |

## Execution Rules

1. Always pass a valid base58 Solana address for `{mint}` or `{wallet}` (32-44 characters).
2. Use `agentcash` to automatically detect the `402 Payment Required` header and settle in USDC on Base or Solana:
   - CLI: `npx agentcash@latest fetch https://godseyex402.dpdns.org/v1/audit/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`
   - MCP: `agentcash.fetch(url="https://godseyex402.dpdns.org/v1/audit/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", method="GET")`
3. Flag the token as high risk if `mint_audit.is_honeypot` is `true`, `holder_audit.is_bundled` is `true`, or `deployer_audit.is_burner` is `true`.
