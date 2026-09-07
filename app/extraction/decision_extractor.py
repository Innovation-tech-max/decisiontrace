import json

from app.llm.client import ask_llm
from app.models.decision import Decision

EXTRACTION_PROMPT = """
You are a decision extraction system.

Analyze the meeting transcript below.

Extract only information explicitly supported by the transcript.

Identify:

1. The final decision
2. Alternatives that were considered
3. The rationale behind the decision
4. Assumptions behind the decision
5. Conditions that should cause the decision to be reconsidered

Do not invent information.

Return ONLY valid JSON in this structure:

{
    "decision": "...",
    "alternatives": [],
    "rationale": [],
    "assumptions": [],
    "review_triggers": []
}

MEETING TRANSCRIPT:
"""

def extract_decision_from_transcript(transcript: str) -> Decision:
    prompt = EXTRACTION_PROMPT + transcript
    response = ask_llm(prompt)
    data = json.loads(response)
    return Decision.model_validate(data)

if __name__ == "__main__":
    with open(
        "data/raw/meeting_001.txt", 
        "r", 
        encoding="utf-8"
    ) as f:
        transcript = f.read()

        decision = extract_decision_from_transcript(transcript)

        print(decision.model_dump_json(indent=2))

        with open(
            "data/processed/decision_001.json", 
            "w", 
            encoding="utf-8"
        ) as out_f:
            out_f.write(decision.model_dump_json(indent=2))