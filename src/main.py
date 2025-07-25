from src.memory import Memory
from src.tools import simulate_tool_response

def interpret_intent(user_input):
    text = user_input.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return "greeting"
    elif "help" in text:
        return "help"
    elif text.startswith("search "):
        return "search"
    elif text.startswith("calculate "):
        return "calculate"
    elif "repeat" in text or "what did i say" in text or "what did i just say" in text:
        return "repeat"
    else:
        return "unknown"

def main():
    memory = Memory()

    print("Welcome to MCP. Type 'exit' to quit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        memory.store("user", user_input)

        intent = interpret_intent(user_input)
        response = simulate_tool_response(intent, user_input, memory)

        memory.store("mcp", response)
        print(f"MCP: {response}")

    print("\nConversation log:")
    for entry in memory.log:
        print(entry)

if __name__ == "__main__":
    main()

