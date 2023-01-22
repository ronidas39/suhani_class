from fastapi import FastAPI

app=FastAPI()

app.get("/")
def index():
    return {"result":"this is index"}