from fastapi import FastAPI

app = FastAPI()

agents = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/agents")
def create_agent(agent_id: str):
    agents[agent_id] = []
    return {"message": f"Agent {agent_id} created"}

@app.post("/tasks")
def create_task(agent_id: str, task: str):
    if agent_id not in agents:
        return {"error": "Agent not found"}
    agents[agent_id].append(task)
    return {"message": "Task added"}

@app.get("/tasks/{agent_id}")
def get_tasks(agent_id: str):
    return {"tasks": agents.get(agent_id, [])}
