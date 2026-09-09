import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b"

def generate(prompt: str, schema: dict | None = None) -> str:
    payload = {"model": MODEL, "prompt": prompt, "stream": False}
    if schema:                       # 有 schema → 强制模型输出 JSON
        payload["format"] = schema
    resp = requests.post(OLLAMA_URL, json=payload, timeout=300)
    resp.raise_for_status()
    return resp.json()["response"]
