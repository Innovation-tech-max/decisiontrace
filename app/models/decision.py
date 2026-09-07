from pydantic import BaseModel, Field

class Decision(BaseModel):
    decision: str = Field(
        description="The decision made by the LLM.",
    )

    alternatives: list[str] = Field(
        default_factory=list,
        description="A list of alternative decisions considered by the LLM.",
    )   

    rationale: list[str] = Field(
        default="",
        description="The rationale behind the decision made by the LLM.",
    )   

    assumptions: list[str] = Field(
        default_factory=list,
        description="A list of assumptions made by the LLM in reaching its decision.",
    )   

    review_triggers: list[str] = Field(
        default_factory=list,
        description="A list of triggers that would prompt a review of the decision.",
    )
