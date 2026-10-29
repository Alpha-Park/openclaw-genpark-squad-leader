# -*- coding: utf-8 -*-
from client import OpenClawGenParkSquadLeader

def main():
    leader = OpenClawGenParkSquadLeader()
    print("=== OpenClaw GenPark Squad Leader Swarm Allocator ===")

    # Register worker agents in the swarm
    leader.register_heartbeat("agent_analyst_1", ["data_analysis", "sql"], current_load=3)
    leader.register_heartbeat("agent_analyst_2", ["data_analysis", "python"], current_load=1)
    leader.register_heartbeat("agent_writer_1", ["copywriting", "seo"], current_load=0)

    # Allocate incoming tasks based on load and capability
    t1 = leader.allocate_task_to_swarm("task_churn_eval", "data_analysis")
    print(f"Task 1 Allocation: Assigned={t1['assigned']} -> Node={t1.get('assigned_to')}")

    t2 = leader.allocate_task_to_swarm("task_blog_post", "copywriting")
    print(f"Task 2 Allocation: Assigned={t2['assigned']} -> Node={t2.get('assigned_to')}")

if __name__ == "__main__":
    main()
