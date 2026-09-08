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
6. Evidence supporting the extracted information

For evidence:
- Use statements directly supported by the transcript.
- Do not invent evidence.
- Include the source filename provided below.

Do not infer facts that are not present in the transcript.

Return ONLY valid JSON in this exact structure:

{
    "decision": "...",
    "alternatives": [],
    "rationale": [],
    "assumptions": [],
    "review_triggers": [],
    "evidence": [
        {
            "text": "...",
            "source": "..."
        }
    ]
}

SOURCE FILE:
meeting_001.txt

MEETING TRANSCRIPT:
"""

def extract_decision(
    transcript: str,
    source: str,
) -> Decision:
    prompt = (
    EXTRACTION_PROMPT
    + f"\nSOURCE FILE: {source}\n\n"
    + transcript
)
    response = ask_llm(prompt)
    data = json.loads(response)
    return Decision.model_validate(data)

if __name__ == "__main__":
    source = "decision_001.txt"

    with open(
        f"data/raw/{source}",
        "r",
        encoding="utf-8",
    ) as file:
        transcript = file.read()

    decision = extract_decision(
        transcript,
        source,
    )

    print(decision.model_dump_json(indent=2))

    with open(
        "data/processed/decision_001.json",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            decision.model_dump_json(indent=2)
        )