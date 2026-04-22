from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.memory import state
from agent.tools import mock_lead_capture

def run_agent():
    print("🤖 AutoStream AI Agent Started!")

    while True:
        user_input = input("You: ")

        intent = detect_intent(user_input)

        # IMPORTANT: if in lead flow, don't override intent
        if not state["stage"]:
            state["intent"] = intent

        if intent == "greeting" and not state["stage"]:
            print("Agent: Hey! 👋 Looking to create amazing videos faster? I can help with plans, pricing, or getting you started.")

        elif intent == "inquiry" and not state["stage"]:
            answer = retrieve_answer(user_input)
            print(f"Agent: {answer}\nLet me know if you'd like help choosing a plan 😊")

        elif intent == "high_intent" or state["stage"]:

            if not state["stage"]:
                print("Agent: Great choice! Let's get you started 🚀")
                print("Agent: What's your name?")
                state["stage"] = "ask_name"
                continue

            if state["stage"] == "ask_name":
                state["name"] = user_input
                print(f"Agent: Nice to meet you {state['name']} 😊")
                print("Agent: What's your email?")
                state["stage"] = "ask_email"
                continue

            if state["stage"] == "ask_email":
                state["email"] = user_input
                print("Agent: Got it 👍 Which platform do you create content on?")
                state["stage"] = "ask_platform"
                continue

            if state["stage"] == "ask_platform":
                platform = user_input.lower()

                valid_platforms = ["youtube", "instagram", "tiktok"]

                if platform not in valid_platforms:
                    print("Agent: Please choose a valid platform (YouTube, Instagram, TikTok)")
                    continue

                state["platform"] = platform

                mock_lead_capture(
                    state["name"],
                    state["email"],
                    state["platform"]
                )

                print("Agent: You're successfully onboarded 🎉")

                # reset
                state["name"] = None
                state["email"] = None
                state["platform"] = None
                state["stage"] = None

                continue


if __name__ == "__main__":
    run_agent()