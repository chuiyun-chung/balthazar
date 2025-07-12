from src.memory import Memory

def main():
    memory = Memory()

    print("Welcome to MCP. Type 'exit' to quit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        memory.store("user", user_input)
        
        # Simulate a response (MCP will be smarter later)
        response = f"You said: {user_input}"
        memory.store("mcp", response)

        print(f"MCP: {response}")

    print("\nConversation log:")
    for entry in memory.log:
        print(entry)

if __name__ == "__main__":
    main()

