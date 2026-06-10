from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """Request model for myth analysis."""

    claim: str = Field(..., min_length=1, max_length=1000)

    class Config:
        json_schema_extra = {
            "example": {"claim": "Vaccines cause autism."}
        }


class AnalyzeResponse(BaseModel):
    """Response model for myth analysis."""

    claim: str
    verdict: str = Field(..., description="TRUE, MOSTLY TRUE, MIXED, MOSTLY FALSE, FALSE, or INSUFFICIENT EVIDENCE")
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence score between 0 and 1")
    explanation: str

    class Config:
        json_schema_extra = {
            "example": {
                "claim": "Vaccines cause autism.",
                "verdict": "FALSE",
                "confidence_score": 0.98,
                "explanation": "Multiple large-scale studies have found no link between vaccines and autism."
            }
        }
