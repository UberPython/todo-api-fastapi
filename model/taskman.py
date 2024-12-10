import json
from typing import List, Optional
from .model import Task, TaskList, ID

filepath = "data/tasks.json"


async def data_to_json(data: List):
    """
    1. Take input data, of a list of tasks
    2. Write the data into a json file (tasks.json)
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)


async def get_tasks(id: Optional[int] = None):
    """
    1. Fetch all tasks if no argument (id) provided
    2. Else fetch the task by id provided
    """
    with open(filepath, 'r') as f:
        tasks = json.load(f)
    
    if id is None:
        return tasks
    
    for task in tasks:
        if task['id'] == id:
            return task
    
    return None


async def create_task(new_task: Task):
    """
    1. Create a new task and add it to the list of tasks
    2. Write the updated tasklist to file
    """
    with open(filepath, 'r') as f:
        tasks = json.load(f)
    
    new_id = max([task['id'] for task in tasks], default=0) + 1
    new_task_list = {'id': new_id, 'task': new_task.dict()}
    tasks.append(new_task_list)
    
    await data_to_json(tasks)
    return new_id


async def delete_task(id: int):
    """
    1. Delete the task by id provided
    """
    with open(filepath, 'r') as f:
        tasks = json.load(f)
    
    tasks = [task for task in tasks if task['id'] != id]
    
    await data_to_json(tasks)
    return id


async def update_task(id: int, new_task: Task):
    """
    1. Update the task by id based on new task details
    2. Write the updated tasklist to file
    """
    with open(filepath, 'r') as f:
        tasks = json.load(f)
    
    for task in tasks:
        if task['id'] == id:
            task['task'] = new_task.dict()
            break
    
    await data_to_json(tasks)
