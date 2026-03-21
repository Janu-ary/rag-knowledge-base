from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "你好"}