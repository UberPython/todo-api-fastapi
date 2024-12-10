from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from model.model import Task, TaskList
import model.taskman as taskman

app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():
    return await taskman.get_tasks()


@app.get("/api/tasks/{id}")
async def get_task(id: int):
    return await taskman.get_tasks(id)


@app.post("/api/tasks/create")
async def create_task(task: Task):
    id = await taskman.create_task(task)
    return await taskman.get_tasks(id)


@app.put("/api/tasks/{id}/update")
async def update_task(id: int, task: Task):
    await taskman.update_task(id, task)
    return await taskman.get_tasks(id)


@app.delete("/api/tasks/{id}/delete")
async def delete_task(id: int):
    id = await taskman.delete_task(id)
    response = {id: "Task successfully deleted"}
    return jsonable_encoder(response)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
