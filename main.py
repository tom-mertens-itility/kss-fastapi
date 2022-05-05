"""Demo script for KSS FastAPI"""
from fastapi import FastAPI, status, HTTPException
import schemas
import json
from datetime import datetime
import uuid
import copy


def load_data():
    """Reads data from json file on disk"""
    with open("data.json", 'r') as f:
        data = json.load(f)
    for user in data['users']:
        data['users'][user]['creationDate'] = datetime.strptime(data['users'][user]['creationDate'],
                                                                "%Y-%m-%d %H:%M:%S.%f")
    return data


data = load_data()
app = FastAPI()


@app.get('/users/', response_model=schemas.ReturnUser)
async def get_user(user_id: str):
    """Will retrieve some basic info about a user"""
    try:
        user_data = data['users'][user_id]
        return user_data
    except KeyError:  # we get an index error if we fill in a nonexistent ID.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReturnUser)
async def create_user(user_request: schemas.CreateUser):
    """Creates a user"""
    user_request = user_request.dict()
    user_request['id'] = str(uuid.uuid4())

    data['users'][user_request['id']] = user_request
    # save into the json file:
    with open("data.json", 'w') as f:
        json.dump(obj=data, fp=f, indent=3, default=str)
    return user_request
