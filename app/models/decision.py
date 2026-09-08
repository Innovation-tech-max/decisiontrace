from pydantic import BaseModel, Field

class Evidence(BaseModel):
    text: str = Field(
        description="Supporting statement from the source."
    )

    source: str = Field(
        description="Speaker or source document containing the evidence."
    )

class Decision(BaseModel):
    decision: str = Field(
        description="The decision made by the team.",
    )

    alternatives: list[str] = Field(
        default_factory=list,
        description="A list of alternative decisions considered.",
    )   

    rationale: list[str] = Field(
        default_factory=list,
        description="The rationale behind the decision made.",
    )   

    assumptions: list[str] = Field(
        default_factory=list,
        description="A list of assumptions made in reaching its decision.",
    )   

    review_triggers: list[str] = Field(
        default_factory=list,
        description="A list of triggers that would prompt a review of the decision.",
    )

    evidence: list[Evidence] = Field(
        default_factory=list,
        description="A list of evidence supporting the decision made.",
    )
