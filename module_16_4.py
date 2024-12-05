from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel



app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age:int

@app.get("/users")
async def get_users() -> List[User]:
     return users

@app.post("/user/{username}/{age}")
async def create_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                       age: Annotated[int, Path(gt=18, le=120, description="Enter age", example='24')]) -> User:
    current_id = 1 if not users else users[-1].id + 1
    current_user = User(id=current_id, username=username, age=age)
    users.append(current_user)
    return current_user

@app.put("/user/{user_id}{username}/{age}")
async def update_users(user_id: Annotated[int, Path(ge=0, le=1000000, description="Enter user_id", example="24")],
                       username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                       example='UrbanProfi')], age: Annotated[int, Path(gt=18, le=120, description="Enter age",
                       example='24')]) -> User:
    for user in users:
        if user.id == user_id:
           user.username == username
           user.age == age
           return user
    raise HTTPException(status_code=404, dataile="The User was not found")

@app.delete("/user/{user_id}")
async def delete_users(user_id: Annotated[int, Path(ge=0, le=1000000, description="Enter user_id",
                       example="24")]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
           deleted_user = user.pop(i)
           return deleted_user
    raise HTTPException(status_code=404, dataile="The User was not found")
