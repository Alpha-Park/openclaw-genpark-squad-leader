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

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
