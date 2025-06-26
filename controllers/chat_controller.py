from models.meta_agent import MetaAgent

class ChatController:
    def __init__(self):
        self.agent = MetaAgent()

    def handle_user_input(self, input_text):
        return self.agent.process(input_text)
