from fastapi import FastAPI

app=FastAPI()

@app.get("/sum/{username}")
def index(username):
    data=""
    return {"data":data}

@app.get("/sub")
def movie():
    return {"sub":20}
