from fastapi import APIRouter, Request
from pymongo import MongoClient
from agents.codeagent import invoke_code_agent
import asyncio
from agents.marketagent import invoke_market_agent

router = APIRouter()
client = MongoClient("mongodb://localhost:27017/")
db = client["judgy"]


@router.get("/crud-agent")
def crudAgent_endpoint():
    return {"message": "Hello from Crud Agent, Okay I'm not really an agent"}


@router.post("/create-project")
async def create_project(request: Request):
    data = await request.json()
    print(data)

    new_project = db.projects.insert_one(data)
    print(new_project.inserted_id)

    asyncio.create_task(invoke_market_agent(str(new_project.inserted_id), data["shortDescription"]))
    asyncio.create_task(invoke_code_agent(data["githubLink"], str(new_project.inserted_id)))    
    return {"message": "Project created", "project_id": str(new_project.inserted_id)}

@router.post("/create-hackathon")
async def create_hackathon(request: Request):
    data = await request.json()
    print(data)

    new_hackathon = db.hackathons.insert_one(data)
    print(new_hackathon.inserted_id)
    
    return {"message": "Hackathon created", "hackathon_id": str(new_hackathon.inserted_id)}

# market agent
# chat agent
# general agent
# create hackathon config
# add all projects
# get all projects
# Search
# get project by id

# analytics