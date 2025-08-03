from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request schema
class MCPRequest(BaseModel):
    method: str
    params: dict | None = None

# MCP endpoint
@app.post("/mcp")
async def handle_mcp(req: MCPRequest):
    if req.method == "ping":
        return {"result": "pong from dev"}
    return {"error": "Unknown method"}
