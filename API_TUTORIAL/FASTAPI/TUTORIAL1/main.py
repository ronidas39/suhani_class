from fastapi import FastAPI
import io

app=FastAPI()


def readFile(name):
    found=0
    with io.open("input.csv","r",encoding="utf-8")as f1:
        data=f1.read()
        f1.close()
    lines=data.split("\n")[1:]
    for line in lines:
        name_from_file=line.split(",")[0]
        if name==name_from_file:
            found=1
            return (line.split(",")[1],line.split(",")[2])
    if(found==0):
        return("NA","NA")


@app.get("/sum/{username}")
def index(username):
    data=""
    return {"data":data}

@app.get("/sub")
def movie():
    return {"sub":20}

@app.get("/search/{name}")
def getResults(name):
    age,city=readFile(name)
    if (age=="NA" and city=="NA"):
        return {"response":f"user {name} not found in file"}
    else:
        return {"age":age,"city":city}


