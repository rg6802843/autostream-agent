def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in text for word in ["price", "plan", "cost", "pricing"]):
        return "inquiry"


    elif any(word in text for word in ["buy", "purchase", "subscribe", "want"]):
        return "high_intent"

    else:
        return "inquiry"