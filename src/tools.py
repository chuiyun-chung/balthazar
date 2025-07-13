def simulate_tool_response(intent, user_input):
    if intent == "greeting":
        return "Hello! 👋 How can I help you today?"
    elif intent == "help":
        return (
            "I can respond to greetings, "
            "simulate search, "
            "or calculate simple expressions."
        )
    elif intent == "search":
        query = user_input[len("search"):].strip()
        return f"🔍 Searching the web for: '{query}'... (simulated)"
    elif intent == "calculate":
        try:
            expression = user_input[len("calculate"):].strip()
            result = eval(expression, {"__builtins__": {}})
            return f"The result is: {result}"
        except Exception:
            return "Sorry, I couldn’t calculate that. Please check your expression."
    else:
        return "I'm still learning. Try saying 'help' to see what I can do."

