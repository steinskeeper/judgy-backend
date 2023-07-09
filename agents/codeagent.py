from langchain.chat_models import ChatVertexAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader
from git import Repo
from langchain.document_loaders import GitLoader
from fastapi import APIRouter
import asyncio

from pymongo import MongoClient
router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["judgy"]

@router.get("/code-agent")
def codeAgent_endpoint():
    return {"message": "Hello from Code Agent"}


async def invoke_code_agent(repolink: str, project_id: str):
    await asyncio.sleep(5)
    DIRECTORY = "projects_source_code/"+project_id
    repo = Repo.clone_from(
        repolink, to_path=DIRECTORY
    )
    branch = repo.head.reference
    loader = GitLoader(repo_path=DIRECTORY, branch=branch)
    llm = ChatVertexAI()
    index = VectorstoreIndexCreator().from_loaders([loader])
    # Get theme from hackathon collection
    technologies = ""
    for x in db.hackathons.find():
        technologies = x["technologies"]
    
    questionToAsk = ["Is the code complete?", "Is the project using the following technologies: ?"+technologies, "Talk about the code quality of the project?"]
    agentAnswers = []
    for question in questionToAsk:
        response = index.query(question, llm)
        agentAnswers.append(response)
    
    # Save the answers to the database
    final = []
    for i in range(len(questionToAsk)):
        newval = {"question": questionToAsk[i], "answer": agentAnswers[i]}
        final.append(newval)
    query = {"_id": project_id}
    newvalues = {"$set": {"codeAgentAnalysis": final}}
    db.projects.update_one(query, newvalues)
    print("Code Agent : Task Complete")


    
