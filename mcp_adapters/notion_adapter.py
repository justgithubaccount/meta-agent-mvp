class NotionMCPAdapter:
    def get_context(self, query):
        # Заглушка — здесь будет реальное подключение к Notion API
        return {
            "source": "Notion",
            "entries": [
                {
                    "title": "Sales Strategy 2024",
                    "summary": "Фокус на B2B SaaS и оптимизацию входящего воронки.",
                    "relevant_to_query": True
                }
            ]
        }
