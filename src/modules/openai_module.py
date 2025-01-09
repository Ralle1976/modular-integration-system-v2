class OpenAIChatGPTModule:
    def __init__(self, api_key: str, default_model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        openai.api_key = api_key
...