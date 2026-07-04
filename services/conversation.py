from services.recommendation import recommend
from services.compare import compare

ROLE_KEYWORDS = [
    "developer", "engineer", "manager", "analyst",
    "java", "python", "sales", "support", "tester",
    "qa", "hr", "accountant"
]

EXPERIENCE_KEYWORDS = [
    "year", "years", "yr", "yrs", "experience",
    "junior", "mid", "senior", "lead",
    "graduate", "entry"
]

OFFTOPIC = [
    "ipl", "movie", "cricket", "weather", "politics"
]


def chat(user_message: str):

    text = user_message.lower()

    # Off-topic
    if any(x in text for x in OFFTOPIC):
        return {
            "reply": "I can only help with SHL assessments.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Comparison
    if "compare" in text or "difference" in text:

        if "opq" in text:
            a = "opq"

            if "gsa" in text:
                b = "gsa"
            else:
                b = ""

            result = compare(a, b)

            if result:
                return {
                    "reply": result["reply"],
                    "recommendations": [],
                    "end_of_conversation": True
                }

    # Clarification
    if not any(x in text for x in ROLE_KEYWORDS):
        return {
            "reply": "Which role are you hiring for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if not any(x in text for x in EXPERIENCE_KEYWORDS):
        return {
            "reply": "What seniority level or years of experience are you looking for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    recs = recommend(user_message)

    return {
        "reply": f"I found {len(recs)} SHL assessments.",
        "recommendations": recs[:10],
        "end_of_conversation": True
    }