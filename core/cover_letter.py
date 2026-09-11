from core.ollama_client import generate
from core.prompts import COVER_PROMPT

def generate_cover_letter(jd: str, resume: str, analysis: dict) -> str:
    prompt = COVER_PROMPT.format(jd=jd, resume=resume, analysis=str(analysis))
    return generate(prompt)
