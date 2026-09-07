from pydantic import BaseModel, Field

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
