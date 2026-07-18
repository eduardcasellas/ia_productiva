import os
import requests
from dotenv import load_dotenv

load_dotenv()

class IAAdapter:
    def __init__(self, model="deepseek"):
        self.model = model
        self.api_key = None
        self.api_url = None
        self._configure()
    
    def _configure(self):
        if self.model == "deepseek":
            self.api_key = os.getenv("DEEPSEEK_API_KEY")
            self.api_url = "https://api.deepseek.com/v1/chat/completions"
        elif self.model == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
            self.api_url = "https://api.openai.com/v1/chat/completions"
        elif self.model == "claude":
            self.api_key = os.getenv("ANTHROPIC_API_KEY")
            self.api_url = "https://api.anthropic.com/v1/messages"
        else:
            raise ValueError(f"Model {self.model} no suportat")
    
    def query(self, prompt, context=None, temperature=0.7, max_tokens=4096):
        if self.model == "deepseek":
            return self._query_deepseek(prompt, context, temperature, max_tokens)
        # Altres models...
    
    def _query_deepseek(self, prompt, context, temperature, max_tokens):
        if not self.api_key:
            raise ValueError("Falta la clau d'API de DeepSeek. Configura DEEPSEEK_API_KEY al .env")
        
        messages = []
        if context:
            messages.append({"role": "system", "content": context})
        messages.append({"role": "user", "content": prompt})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error: {e}")
            return None