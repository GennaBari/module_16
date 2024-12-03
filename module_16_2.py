from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
     return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admins():
     return {"message": "Вы вошли как администратор"}

@app.get("/users/{user_id}")
async def get_id_users(user_id: Annotated[int, Path(gt=1, le=1000, description="Enter User ID", example='1')]) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/users/{username}/{age}")
async def get_name_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')]
                         , age: Annotated[int, Path(gt=18, le=120, description="Enter age", example='24')]) -> dict:
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

