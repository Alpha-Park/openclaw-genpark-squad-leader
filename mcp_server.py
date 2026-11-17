# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkSquadLeader

leader = OpenClawGenParkSquadLeader()

def run_tool(name, args):
    if name == "register_heartbeat":
        a_id = args.get("agent_id", "worker_01")
        caps = args.get("capabilities", [])
        load = int(args.get("current_load", 0))
        return leader.register_heartbeat(a_id, caps, load)
    elif name == "allocate_task_to_swarm":
        t_id = args.get("task_id", "task_001")
        cap = args.get("required_capability", "code_review")
        wt = int(args.get("task_weight", 1))
        return leader.allocate_task_to_swarm(t_id, cap, wt)
    else:
        raise ValueError(f"Unknown tool: {name}")

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('openclaw-genpark-squad-leader')

@mcp.tool()
def register_heartbeat(agent_id: str = "worker_01", capabilities: Optional[List[str]] = None, current_load: int = 0) -> str:
    """Register a worker heartbeat in the local swarm state."""
    return json.dumps(run_tool('register_heartbeat', {'agent_id': agent_id, 'capabilities': capabilities if capabilities is not None else [], 'current_load': current_load}))

@mcp.tool()
def allocate_task_to_swarm(task_id: str = "task_001", required_capability: str = "code_review", task_weight: int = 1) -> str:
    """Allocate a task using the registered local swarm state."""
    return json.dumps(run_tool('allocate_task_to_swarm', {'task_id': task_id, 'required_capability': required_capability, 'task_weight': task_weight}))

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw Squad Leader Self-Test...")
        leader.register_heartbeat("worker_alpha", ["nlp", "vision"], current_load=2)
        leader.register_heartbeat("worker_beta", ["nlp"], current_load=0)
        res = leader.allocate_task_to_swarm("task_99", "nlp")
        assert res["assigned"] is True
        assert res["assigned_to"] == "worker_beta" # Lowest load
        print("[TEST] All tests passed successfully!")
        return

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
