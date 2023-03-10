from fastapi import APIRouter
from models.tasks import Task
from config.db import conn
from schema.tasks import tasksEntity, taskEntity
from bson import ObjectId as objectID

tasks = APIRouter()
@tasks.get("/")
async def root():
    return {"message": "Hello World"}

@tasks.get("/tasks")
async def find_all_tasks():
    # print no tasks if  no tasks are present
    if conn.db.tasks.count_documents({}) == 0:
        return {"message": "no tasks found, please add some tasks"}
    return tasksEntity(conn.db.tasks.find())


@tasks.get(path="/tasks/:id")
async def find_task_by_id(id):
    # find task based on id and id does not exist then return no task found

    if conn.db.tasks.count_documents({"_id": objectID(id)}) == 0:
        return {"message": "no task found associated with this id"}

    return taskEntity(conn.db.tasks.find_one({"_id": objectID(id)}))


@tasks.post("/tasks")
async def create_tasks(task: Task):
    conn.db.tasks.insert_one(dict(task))
    # return only the last task
    return taskEntity(conn.db.tasks.find().sort("_id", -1).limit(1)[0])


@tasks.put(path="/tasks/{id}")
async def update_task_by_id(id, task: Task):
    if conn.db.tasks.count_documents({"_id": objectID(id)}) == 0:
        return {"message": "no task found associated with this id"}
    conn.db.tasks.find_one_and_update({"_id": objectID(id)}, {"$set": dict(task)})
    return taskEntity(conn.db.tasks.find_one({"_id": objectID(id)}))


@tasks.delete(path="/tasks/{id}")
async def delete_task_by_id(id):
    if conn.db.tasks.count_documents({"_id": objectID(id)}) == 0:
        return {"message": "no task found associated with this id"}
    conn.db.tasks.delete_one({"_id": objectID(id)})
    return {"message": "task deleted successfully"}


@tasks.delete("/tasks")
async def delete_all_tasks():
    if conn.db.tasks.count_documents({}) == 0:
        return {"message": "no tasks found, please add some tasks"}
    conn.db.tasks.delete_many({})
    return {"message": "all tasks deleted successfully"}


@tasks.post("/tasks/{id}/complete")
async def complete_task_by_id(id):
    # if task is not present then return no task found
    if conn.db.tasks.count_documents({"_id": objectID(id)}) == 0:
        return {"message": "no task found associated with this id"}
    conn.db.tasks.update_one({"_id": objectID(id)}, {"$set": {"complete": True}})
    return taskEntity(conn.db.tasks.find_one({"_id": objectID(id)}))


@tasks.post("/tasks/{id}/incomplete")
async def incomplete_task_by_id(id):
    if conn.db.tasks.count_documents({"_id": objectID(id)}) == 0:
        return {"message": "no task found associated with this id"}
    conn.db.tasks.update_one({"_id": objectID(id)}, {"$set": {"complete": False}})
    return taskEntity(conn.db.tasks.find_one({"_id": objectID(id)}))


@tasks.post("/tasks/complete")
async def complete_all_tasks():
    if conn.db.tasks.count_documents({}) == 0:
        return {"message": "no tasks found, please add some tasks"}
    conn.db.tasks.update_many({}, {"$set": {"complete": True}})
    return tasksEntity(conn.db.tasks.find())


@tasks.post("/tasks/incomplete")
async def incomplete_all_tasks():
    # if tasks are npot present then return no tasks found
    if conn.db.tasks.count_documents({}) == 0:
        return {"message": "no tasks found, please add some tasks"}
    conn.db.tasks.update_many({}, {"$set": {"complete": False}})
    return tasksEntity(conn.db.tasks.find())
