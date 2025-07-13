from src.memory import Memory
from src.tools import simulate_tool_response

def interpret_intent(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "greeting"
    elif "help" in user_input:
        return "help"
    elif user_input.startswith("search"):
        return "search"
    elif user_input.startswith("calculate"):
        return "calculate"
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
        response = simulate_tool_response(intent, user_input)

        memory.store("mcp", response)
        print(f"MCP: {response}")

    print("\nConversation log:")
    for entry in memory.log:
        print(entry)

if __name__ == "__main__":
    main()

