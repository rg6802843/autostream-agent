import json

with open("data/knowledge.json") as f:
    knowledge = json.load(f)

def retrieve_answer(query):
    query = query.lower()

    # handle pricing keyword
    if "price" in query or "pricing" in query:
        return (
            "We offer two plans:\n"
            "Basic Plan: $29/month (10 videos, 720p)\n"
            "Pro Plan: $79/month (Unlimited videos, 4K, AI captions)"
        )

    for key in knowledge:
        if key in query:
            return knowledge[key]

    return "I can help with pricing, plans, and policies. What would you like to know?"