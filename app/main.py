from fastapi import FastAPI
from routes.tasks import tasks

app = FastAPI()
app.include_router(tasks)
