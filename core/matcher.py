import json
from core.ollama_client import generate
from core.prompts import MATCH_PROMPT

SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "integer"},
        "matched_skills": {"type": "array", "items": {"type": "string"}},
        "missing_skills": {"type": "array", "items": {"type": "string"}},
        "suggestions": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["score", "matched_skills", "missing_skills", "suggestions"]
}

def analyze(jd: str, resume: str) -> dict:
    prompt = MATCH_PROMPT.format(jd=jd, resume=resume)
    raw = generate(prompt, SCHEMA)
    return json.loads(raw)
