from mcp_adapters.notion_adapter import NotionMCPAdapter

class MetaAgent:
    def __init__(self):
        self.context_adapter = NotionMCPAdapter()

    def process(self, user_prompt):
        context = self.context_adapter.get_context(user_prompt)
        context_text = "\n".join([entry['summary'] for entry in context["entries"]])
        return f"📚 Context:\n{context_text}\n\n💡 Запрос: {user_prompt}"
