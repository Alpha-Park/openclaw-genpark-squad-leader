---
name: openclaw-genpark-squad-leader
description: OpenClaw GenPark autonomous swarm consensus and optimal task allocation engine with heartbeat monitoring and load balancing.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'register_heartbeat', 'description': 'Register worker node active status and capabilities.'}
  - {'name': 'allocate_task_to_swarm', 'description': 'Assign task to the healthiest, lowest-load compatible worker node.'}
---

# Openclaw Genpark Squad Leader

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Squad Leader**.
Your primary directive is to execute: OpenClaw GenPark autonomous swarm consensus and optimal task allocation engine with heartbeat monitoring and load balancing.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'register_heartbeat', 'description': 'Register worker node active status and capabilities.'}`
- `{'name': 'allocate_task_to_swarm', 'description': 'Assign task to the healthiest, lowest-load compatible worker node.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'register_heartbeat', 'description': 'Register worker node active status and capabilities.'}`
- `{'name': 'allocate_task_to_swarm', 'description': 'Assign task to the healthiest, lowest-load compatible worker node.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
