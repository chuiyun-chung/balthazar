class Memory:
    def __init__(self):
        self.log = []

    def store(self, speaker, text):
        self.log.append({"speaker": speaker, "text": text})

    def last_user_message(self):
        # Skip the most recent user message (i.e. the one currently being processed)
        count = 0
        for entry in reversed(self.log):
            if entry["speaker"] == "user":
                count += 1
                if count == 2:
                    return entry["text"]
        return None

    def last_mcp_message(self):
        for entry in reversed(self.log):
            if entry["speaker"] == "mcp":
                return entry["text"]
        return None

