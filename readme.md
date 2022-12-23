This is the start of a series of learning that I am trying to do using ChatGPT. Instead of asking ChatGPT to give me solutions to my problems, the idea is to ask it to give me problems that I can solve and learn. The first problem I asked it to give me was a backend assignment that involves me using FastAPI to build a todo list app. This is the implementation of the same, as this series goes on I will take up tougher problems too. It has even told me to host the app on glitch. so will be doing that.

### Requirements
- python3
- git

### Installation
git clone git@github.com:SammithSB/todo-list-fastapi.git
python3 -r requirements.txt
#### setup .env file with the following line as data
#### MONGO_URI_="your_mongo_uri"
uvicorn app:app --reload


### Usage
For local usage, running the above command will start the server at [http://localhost:8000](http://localhost:8000)

Otherwise the deployed API can be accessed at [to-be-done](to-be-done)

### Available endpoints are

    -   `POST /tasks`: Creates a new task. The request body should include the task description and a boolean value indicating whether the task is completed.
    -   `GET /tasks`: Retrieves a list of all tasks.
    -   `GET /tasks/{id}`: Retrieves a single task by its ID.
    -   `PUT /tasks/{id}`: Updates an existing task. The request body should include the updated task description and completion status.
    -   `DELETE /tasks/{id}`: Deletes a task.
    -   `POST /tasks/{id}/complete`: Marks a task as completed.
    -   `POST /tasks/{id}/incomplete`: Marks a task as incomplete.
    -   `POST /tasks/complete`: Marks all tasks as completed.
    -   `POST /tasks/incomplete`: Marks all tasks as incomplete.
    -   `DELETE /tasks`: Deletes all tasks.