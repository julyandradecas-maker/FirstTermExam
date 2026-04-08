from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


class User(SQLModel):
    id: int = 0
    username: str
    password: str
    email: str = ""
    is_active: bool = True


db_users = [
    User(id=1, username="admin", password="ad", email="admin@mail.com"),
    User(id=2, username="user", password="user", email="user@mail.com"),
    User(id=3, username="guest", password="guest", email="guest@mail.com"),
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users")
def create_user(user: User):
    for db_user in db_users:
        if db_user.username == user.username:
            return {"error": "Username ya existe"}
    user.id = len(db_users) + 1
    db_users.append(user)
    return user


@app.get("/users")
def get_users():
    return db_users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in db_users:
        if user.id == user_id:
            return user
    return {"error": "Usuario no encontrado"}


@app.put("/users/{user_id}")
def update_user(user_id: int, data: User):
    for user in db_users:
        if user.id == user_id:
            user.username = data.username
            user.email = data.email
            user.is_active = data.is_active
            return user
    return {"error": "Usuario no encontrado"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(db_users):
        if user.id == user_id:
            db_users.pop(i)
            return {"message": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}


@app.post("/login")
def login(user: User):
    for db_user in db_users:
        if db_user.username == user.username and db_user.password == user.password:
            return {"success": True, "message": f"Bienvenido, {user.username}"}
    return {"success": False, "message": "Usuario o contraseña incorrectos"}