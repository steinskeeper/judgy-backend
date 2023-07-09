from fastapi import APIRouter

router = APIRouter()

@router.get("/chat-agent")
def chatAgent_endpoint():
    return {"message": "Hello from Chat Agent"}

def invoke_chat_agent():
    return {"message": "Hello from Chat Agent"}