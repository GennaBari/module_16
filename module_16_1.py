from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
     return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admins():
     return {"message": "Вы вошли как администратор"}

@app.get("/users/{user_id}")
async def get_id_users(user_id: int) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/users/{user_name}/{age}")
async def get_name_users(username:str, age: str) -> dict:
     return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}



