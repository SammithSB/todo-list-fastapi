FROM python:3.10


EXPOSE 8000

WORKDIR /usr/src/todo-list-fastapi

ENV PORT 8000
ENV HOST "0.0.0.0"
COPY ./config/ /todo-list-fastapi/config
COPY ./schema/ /todo-list-fastapi/schema
COPY ./routes/ /todo-list-fastapi/routes
COPY ./models/ /todo-list-fastapi/models

COPY ./requirements.txt /todo-list-fastapi
WORKDIR /todo-list-fastapi

RUN pip install -r requirements.txt





CMD ["uvicorn", "main:app"]