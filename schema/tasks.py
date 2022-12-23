def taskEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "description":item["description"],
        "complete":item["complete"]
    }
# above is for a single task but to show for all the tasks we need a list that contains all task which is defined in tasksEntity
def tasksEntity(entity)->list:
    return [taskEntity(item) for item in entity]