from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse, Recommendation 
from services.conversation import chat


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_api(request: ChatRequest):

    # 🔥 build full conversation context
    conversation = "\n".join(
        [f"{m.role}: {m.content}" for m in request.messages]
    )

    result = chat(conversation)

    recommendations = [
        Recommendation(
            name=r["name"],
            url=r["url"],
            test_type=", ".join(r.get("keywords", [])),
            score=r.get("score", 0.0)
        )
        for r in result["recommendations"]
    ]

    return ChatResponse(
        reply=result["reply"],
        recommendations=recommendations,
        end_of_conversation=result["end_of_conversation"]
    )