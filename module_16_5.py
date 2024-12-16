
from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="templates")


app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age:int

@app.get("/")
async def main_page(requests: Request) -> HTMLResponse:
     return templates.TemplateResponse("users.html", {"request":requests, "messages": users})

@app.get("/users/{user_id}")
async def get_users(requests: Request, user_id: int) ->  HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request":requests, "messages": users[user_id -1]})
    except IndexError:
        raise HTTPException(status_code=404, datail="Message not found")


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(gt=18, le=120, description="Enter age")]) -> User:
    if len(users) != 0:
        new_id = 1
    else:
        new_id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_users(user_id: Annotated[int, Path(ge=0, le=1000000, description="Enter user_id", )],
                       username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                       age: Annotated[int, Path(gt=18, le=120, description="Enter age")]) -> User:
    for user in users:
        if user.id == user_id:
           user.username == username
           user.age == age
           return user
        else:
            raise HTTPException(status_code=404, dataile="The User was not found")

@app.delete("/user/{user_id}")
async def delete_users(user_id: int) -> str:
    for i, user in enumerate(users):
        if user.id == user_id:
           deleted_user = user.pop(i)
           return user.pop(i)
    else:
        raise HTTPException(status_code=404, dataile="The User was not found")
