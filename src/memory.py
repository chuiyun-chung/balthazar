class Memory:
    def __init__(self):
        self.log = []

    def store(self, speaker, text):
        self.log.append({"speaker": speaker, "text": text})

