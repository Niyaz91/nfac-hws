from fastapi import FastAPI

app = FastAPI()

@app.get("/index")
def read_index():
    return {"message": "Hello from /index"}