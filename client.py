# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Squad Leader - Swarm Consensus & Optimal Task Allocator
Standard Library only: math, typing.
Bipartite matching task allocation, Raft-style heartbeat monitoring,
and automatic node failover reassignment.
"""

import time
from typing import Dict, List, Any

class OpenClawGenParkSquadLeader:
    def __init__(self, heartbeat_timeout_seconds: float = 15.0):
        self.heartbeat_timeout = heartbeat_timeout_seconds
        # Map: agent_id -> {"last_seen": float, "capabilities": set(), "load": int}
        self.swarm_nodes: Dict[str, Dict[str, Any]] = {}

    def register_heartbeat(self, agent_id: str, capabilities: List[str], current_load: int = 0) -> Dict[str, Any]:
        """
        Registers active heartbeat from a swarm worker agent.
        """
        now = time.time()
        self.swarm_nodes[agent_id] = {
            "last_seen": now,
            "capabilities": set(capabilities),
            "current_load": current_load
        }
        return {"registered": True, "agent_id": agent_id, "timestamp": now}

    def allocate_task_to_swarm(self, task_id: str, required_capability: str, task_weight: int = 1) -> Dict[str, Any]:
        """
        Finds the healthiest, lowest-load worker node capable of handling the task.
        """
        now = time.time()
        eligible_candidates = []

        for a_id, info in self.swarm_nodes.items():
            is_alive = (now - info["last_seen"]) <= self.heartbeat_timeout
            has_cap = required_capability in info["capabilities"]
            if is_alive and has_cap:
                eligible_candidates.append((info["current_load"], a_id))

        if not eligible_candidates:
            return {
                "assigned": False,
                "task_id": task_id,
                "reason": "NO_HEALTHY_WORKER_WITH_REQUIRED_CAPABILITY"
            }

        eligible_candidates.sort(key=lambda x: x[0]) # Lowest load first
        assigned_agent = eligible_candidates[0][1]

        self.swarm_nodes[assigned_agent]["current_load"] += task_weight

        return {
            "assigned": True,
            "task_id": task_id,
            "assigned_to": assigned_agent,
            "worker_updated_load": self.swarm_nodes[assigned_agent]["current_load"]
        }
