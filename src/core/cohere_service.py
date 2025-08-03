import cohere
from src.config.settings import COHERE_API_KEY, MAX_TOKENS, TEMPERATURE, MODEL

class CohereClient:
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)
        self.model = MODEL
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS

    def get_response(self, message: str) -> str:
        response = self.client.chat(
            message=f"answer without using (# **) {message}",
            model=self.model,
            temperature=self.temperature
        )
        return response.text
