import asyncio
from fastapi import APIRouter
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import VertexAI
from pymongo import MongoClient

search = DuckDuckGoSearchRun()

router = APIRouter()
client = MongoClient("mongodb://localhost:27017/")
db = client["judgy"]

@router.get("/market-agent")
async def marketAgent_endpoint():
    await asyncio.sleep(5)
    return {"message": "Hello from Market Agent"}


async def invoke_market_agent(project_id: str, idea: str):
    await asyncio.sleep(5)
    llm = VertexAI(model_name="text-bison@001")
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="useful for when you need to ask with search",
        )
    ]
    marketQuestion = ["target audience",
                      "current market competitors", "potential", "pitfalls", "market size"]
    agentAnswers = []
    def getAnswer(question):
        self_ask_with_search = initialize_agent(
            tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
        )
        prompt = """
        You are a market researcher. You have to answer the question about the idea.
        Idea: {idea}
        Question: {question}
        Rules for answering: 
            1. Use statistical data where ever possible.
            2. Remember to answer like a market researcher.
            3. Answer the question as best you can, in a paragraph.
        """
        prompt = prompt.format(question=question, idea=idea)
        resp = self_ask_with_search.run(prompt)
        agentAnswers.append(resp)
    for i in marketQuestion:
        getAnswer(i)
    
    final = []
    for i in range(len(marketQuestion)):
        newval = {"question": marketQuestion[i], "answer": agentAnswers[i]}
        final.append(newval)
    query = {"_id": project_id}
    newvalues = {"$set": {"marketAgentAnalysis": final}}
    db.projects.update_one(query, newvalues)
    print("Market Agent : Task Complete")
    
