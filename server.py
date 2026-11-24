import base64
import json
import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://godseyex402.dpdns.org"
mcp = FastMCP("gods-eye-solana-audit")


async def _fetch_x402(path: str) -> dict:
    url = f"{BASE_URL}{path}"
    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.get(url)

    if resp.status_code == 200:
        return {"status": 200, "data": resp.json()}

    if resp.status_code == 402:
        payment_header = resp.headers.get("payment-required") or resp.headers.get("x-payment-required")
        challenge = None
        if payment_header:
            try:
                padded = payment_header + "=" * (-len(payment_header) % 4)
                challenge = json.loads(base64.b64decode(padded).decode("utf-8"))
            except Exception:
                challenge = payment_header
        elif resp.text:
            try:
                challenge = resp.json()
            except Exception:
                challenge = resp.text

        return {
            "status": 402,
            "payment_required": True,
            "endpoint": url,
            "how_to_pay": (
                f"This endpoint requires an x402 USDC payment (Base or Solana). "
                f"Run via AgentCash CLI: npx agentcash@latest fetch {url}"
            ),
            "x402_challenge": challenge,
        }

    return {"status": resp.status_code, "endpoint": url, "error": resp.text}


@mcp.tool()
async def get_api_catalog() -> dict:
    """Fetch live pricing, schemas, and x-guidance from God's Eye OpenAPI spec (free)."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(f"{BASE_URL}/openapi.json")
        resp.raise_for_status()
        return resp.json()


@mcp.tool()
async def audit_solana_token(mint: str) -> dict:
    """
    Audit a Solana SPL token mint for honeypot authorities, Top-9 holder bundle %,
    and live 5m DEX order-flow telemetry ($0.03 USDC via x402).
    """
    return await _fetch_x402(f"/v1/audit/{mint.strip()}")


@mcp.tool()
async def inspect_solana_deployer(wallet: str) -> dict:
    """
    Inspect a Solana deployer wallet's age, recent tx count, and burner status
    ($0.02 USDC via x402).
    """
    return await _fetch_x402(f"/v1/deployer/{wallet.strip()}")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
