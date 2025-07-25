class Memory:
    def __init__(self):
        self.log = []

    def store(self, speaker, text):
        self.log.append({"speaker": speaker, "text": text})

    def last_user_message(self):
        for entry in reversed(self.log):
            if entry["speaker"] == "user":
                return entry["text"]
        return None

    def last_mcp_message(self):
        for entry in reversed(self.log):
            if entry["speaker"] == "mcp":
                return entry["text"]
        return None

