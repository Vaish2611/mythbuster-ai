"""Claim parser module for categorizing and extracting claim information."""

import re
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ClaimDomain(str, Enum):
    """Supported domains for claim categorization."""

    HEALTH = "Health"
    SCIENCE = "Science"
    HISTORY = "History"
    POLITICS = "Politics"
    FINANCE = "Finance"
    TECHNOLOGY = "Technology"
    IMMIGRATION = "Immigration"
    GENERAL = "General"


class ParsedClaim(BaseModel):
    """Parsed claim information."""

    claim: str = Field(..., description="The original claim")
    domain: ClaimDomain = Field(..., description="The category/domain of the claim")
    keywords: list[str] = Field(default_factory=list, description="Extracted keywords from the claim")

    class Config:
        json_schema_extra = {
            "example": {
                "claim": "Vaccines cause autism.",
                "domain": "Health",
                "keywords": ["vaccines", "autism", "cause"]
            }
        }


class ClaimParser:
    """Parser for extracting and categorizing claim information."""

    # Domain keywords mapping
    DOMAIN_KEYWORDS = {
        ClaimDomain.HEALTH: [
            "vaccine", "disease", "cure", "treatment", "drug", "medicine", "doctor",
            "hospital", "symptom", "health", "illness", "virus", "bacteria", "infection",
            "cancer", "diabetes", "autism", "covid", "coronavirus", "pandemic"
        ],
        ClaimDomain.SCIENCE: [
            "science", "physics", "chemistry", "biology", "research", "study", "experiment",
            "theory", "atom", "molecule", "energy", "climate", "evolution", "gravity",
            "radiation", "quantum", "universe", "planet", "space", "astronomical"
        ],
        ClaimDomain.HISTORY: [
            "history", "historical", "century", "war", "battle", "revolution", "ancient",
            "medieval", "empire", "dynasty", "civilization", "historical figures",
            "president", "king", "queen", "napoleon", "hitler", "jfk"
        ],
        ClaimDomain.POLITICS: [
            "election", "vote", "political", "government", "president", "congress",
            "senate", "democrat", "republican", "political party", "legislation",
            "law", "immigration", "border", "campaign"
        ],
        ClaimDomain.FINANCE: [
            "economy", "stock", "investment", "money", "bank", "financial", "bitcoin",
            "cryptocurrency", "price", "inflation", "recession", "debt", "trade",
            "tax", "income", "wage", "unemployment"
        ],
        ClaimDomain.TECHNOLOGY: [
            "technology", "ai", "artificial intelligence", "computer", "internet",
            "software", "hardware", "smartphone", "app", "website", "robot",
            "automation", "5g", "quantum computing", "technology"
        ],
        ClaimDomain.IMMIGRATION: [
            "immigration", "immigrant", "refugee", "asylum", "border", "visa",
            "citizenship", "deportation", "migrant", "undocumented", "emigrant"
        ]
    }

    @staticmethod
    def extract_keywords(claim: str, max_keywords: int = 5) -> list[str]:
        """
        Extract keywords from claim.

        Args:
            claim: The claim text
            max_keywords: Maximum number of keywords to extract

        Returns:
            List of extracted keywords
        """
        # Remove common words and extract meaningful terms
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "is", "are", "was", "were", "be", "been", "being", "have", "has",
            "do", "does", "did", "will", "would", "should", "could", "may", "might"
        }

        # Convert to lowercase and split into words
        words = re.findall(r'\b\w+\b', claim.lower())

        # Filter out stop words and short words
        keywords = [
            w for w in words
            if w not in stop_words and len(w) > 2
        ]

        # Remove duplicates while preserving order
        seen = set()
        unique_keywords = []
        for w in keywords:
            if w not in seen:
                seen.add(w)
                unique_keywords.append(w)

        return unique_keywords[:max_keywords]

    @classmethod
    def categorize_domain(cls, claim: str) -> ClaimDomain:
        """
        Categorize claim into a domain based on keywords.

        Args:
            claim: The claim text

        Returns:
            The determined ClaimDomain
        """
        claim_lower = claim.lower()
        domain_scores = {domain: 0 for domain in ClaimDomain}

        # Score each domain based on keyword matches
        for domain, keywords in cls.DOMAIN_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in claim_lower:
                    domain_scores[domain] += 1

        # Return domain with highest score, default to GENERAL
        max_domain = max(domain_scores, key=domain_scores.get)
        return max_domain if domain_scores[max_domain] > 0 else ClaimDomain.GENERAL

    @classmethod
    def parse(cls, claim: str) -> ParsedClaim:
        """
        Parse a claim string and extract information.

        Args:
            claim: The claim to parse

        Returns:
            ParsedClaim object with extracted information
        """
        if not claim or not isinstance(claim, str):
            raise ValueError("Claim must be a non-empty string")

        claim = claim.strip()

        # Categorize the claim
        domain = cls.categorize_domain(claim)

        # Extract keywords
        keywords = cls.extract_keywords(claim)

        return ParsedClaim(
            claim=claim,
            domain=domain,
            keywords=keywords
        )


def parse_claim(claim: str) -> ParsedClaim:
    """
    Convenience function to parse a claim.

    Args:
        claim: The claim to parse

    Returns:
        ParsedClaim object
    """
    return ClaimParser.parse(claim)
