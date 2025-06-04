from fastapi import FastAPI
from app.database import Base, engine
from app.routes import team, comment
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import project, task, comment, team
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

# создаём таблицы (только на этапе тестов)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Task Manager is running"}


Base.metadata.create_all(bind=engine)

app.include_router(project.router)
app.include_router(task.router)
app.include_router(team.router)
app.include_router(comment.router)

from app.routes import auth
app.include_router(auth.router)
