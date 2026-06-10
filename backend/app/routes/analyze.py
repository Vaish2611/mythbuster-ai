"""Analysis routes."""

from fastapi import APIRouter, Depends

from app.models import AnalyzeRequest, AnalyzeResponse
from app.services.analyzer import MythAnalyzerService, get_analyzer_service

router = APIRouter(tags=["analysis"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_claim(
    request: AnalyzeRequest,
    analyzer: MythAnalyzerService = Depends(get_analyzer_service)
) -> AnalyzeResponse:
    """
    Analyze a claim and return verdict with confidence score.
    
    Args:
        request: The claim to analyze
        analyzer: Analyzer service instance
        
    Returns:
        Analysis result with verdict and confidence score
    """
    result = analyzer.analyze(request.claim)
    return AnalyzeResponse(**result)
