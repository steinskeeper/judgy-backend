from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
from agents.marketagent import router as marketAgent_router
from agents.codeagent import router as codeAgent_router
from agents.chatagent import router as chatAgent_router
from agents.crudagent import router as crudAgent_router
import os
load_dotenv()
app = FastAPI()

app.include_router(marketAgent_router, prefix="/api", tags=["Market Agent"])
app.include_router(codeAgent_router, prefix="/api", tags=["Code Agent"])
app.include_router(chatAgent_router, prefix="/api", tags=["Chat Agent"])
app.include_router(crudAgent_router, prefix="/api", tags=["CRUD Agent"])
# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

@app.get("/api")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)