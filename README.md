# Mythbuster-ai
MythBuster AI is an intelligent multi-agent platform designed to combat misinformation by not only determining whether a claim is true or false but also explaining why the claim exists, how it spreads, and what evidence supports or contradicts it.

In an era where misinformation spreads faster than verified information, users are often left with fragmented answers, biased opinions, and a lack of trustworthy explanations. Traditional fact-checking systems typically provide binary verdicts such as "True" or "False" without offering transparency into the reasoning process. MythBuster AI addresses this challenge through a network of collaborative AI agents that investigate claims, gather evidence, analyze bias, identify misinformation patterns, and generate human-friendly explanations.

The platform acts as an AI-powered truth investigation system capable of helping students, professionals, researchers, and the general public make informed decisions based on credible information.

## Problem Statement

The internet contains an overwhelming amount of conflicting information related to healthcare, education, finance, technology, public policy, and everyday life. Users frequently encounter claims such as:

Vaccines cause autism.
AI will replace all jobs.
A master's degree is never worth taking a loan for.
Drinking alkaline water cures diseases.
Social media algorithms intentionally suppress certain viewpoints.
Existing search engines and chatbots often return information without explaining source quality, evidence strength, logical fallacies, or misinformation origins.

## As a result:

Users struggle to evaluate credibility.
Misinformation spreads rapidly through social media.
False claims gain traction through repetition and emotional appeal.
Individuals lack tools to critically assess information.
MythBuster AI aims to become an intelligent evidence-based reasoning system that helps users understand the complete story behind any claim.

## Solution

MythBuster AI leverages a multi-agent architecture built on Azure AI Foundry and Microsoft Agent Framework technologies.

Instead of relying on a single large language model, multiple specialized agents collaborate to investigate a claim from different perspectives.

Each agent contributes expertise to a specific part of the reasoning process, resulting in more accurate, transparent, and explainable outcomes.

## Agent Architecture

Claim Extraction Agent: The Claim Extraction Agent identifies the core factual claim from user input.

Example:

Input:
"People say taking student loans for a master's degree is never worth it."

Extracted Claim:
"A master's degree financed through student loans is never worth the investment."

## Responsibilities:

Remove noise and opinions
Normalize statements
Generate structured claims
Identify sub-claims
Evidence Discovery Agent
This agent searches authoritative sources including:

Government databases
Academic journals
Peer-reviewed publications
News organizations
Public datasets
Healthcare repositories
Responsibilities:

Retrieve evidence
Rank source credibility
Gather supporting and contradicting information
Build evidence packages
Verification Agent
The Verification Agent evaluates evidence and generates a verdict.

## Possible Outcomes:

True
Mostly True
Mixed
Mostly False
False
Insufficient Evidence
Responsibilities:

## Evaluate evidence quality
Calculate confidence scores
Generate reasoning chains
Explain uncertainty
Bias and Manipulation Detection Agent
Many viral claims spread because of cognitive biases rather than evidence.

This agent identifies:

Confirmation bias
Survivorship bias
Selection bias
Emotional framing
Cherry-picked statistics
Misleading correlations
Responsibilities:

Detect manipulation patterns
Explain persuasive techniques
Highlight reasoning flaws
Counter-Perspective Agent
One of the most important features of MythBuster AI is its ability to generate balanced viewpoints.

## Responsibilities:

Present alternative perspectives
Explain opposing arguments
Highlight areas of disagreement
Reduce echo-chamber effects
Myth Origin Tracing Agent
This is the platform's flagship capability.

Instead of simply debunking a myth, the system investigates:

Where the claim originated
How it spread
Which communities amplified it
How it evolved over time
The output is a visual misinformation timeline that helps users understand the lifecycle of a belief.

## Example:

Original Publication
↓
Media Amplification
↓
Social Media Spread
↓
Public Acceptance

Explainability Agent
Different users require different levels of explanation.

This agent generates:

30-second summary
2-minute explanation
Deep-dive analysis
Responsibilities:

Simplify complex information
Adapt explanations to audience expertise
Improve accessibility
Key Features

Evidence-Based Truth Score

Every claim receives:

Confidence Score
Evidence Strength Score
Source Reliability Score
Misinformation Risk Score
This enables users to quickly evaluate credibility.

Source Transparency Dashboard

## Users can inspect:

Supporting sources
Contradicting sources
Evidence ranking
Publication credibility
This promotes trust and transparency.

Interactive Myth Timeline

## Visualizes:

Claim origin
Major amplification events
Viral spread patterns
Current status
Personalized Learning Mode

## Users can ask:

Why is this claim false?
Why do people believe it?
What evidence supports the opposite view?
This transforms MythBuster AI from a fact-checker into a learning platform.

## Technology Stack

AI and Agents

Azure AI Foundry
Azure AI Agents
Azure OpenAI Service
Semantic Kernel
Search and Retrieval

Azure AI Search
Bing Grounding
Vector Search
Backend

Python
FastAPI
Azure Functions
Frontend

Next.js
React
TypeScript
Tailwind CSS
Database

Azure Cosmos DB
Visualization

D3.js
Mermaid
Chart.js
Social Impact

## MythBuster AI contributes to:

Digital literacy
Responsible AI usage
Evidence-based decision making
Reduction of misinformation
Improved public understanding of science and technology
The platform empowers users to think critically rather than simply accepting information at face value.

## Future Roadmap

Phase 1: Health and medical misinformation

Phase 2: Finance and investment myths

Phase 3: Technology and AI misinformation

Phase 4: Educational and career guidance

Phase 5: Global multilingual misinformation monitoring

## Vision

Our vision is to create an AI-powered truth ecosystem that helps individuals navigate the modern information landscape with confidence, transparency, and critical thinking.

Rather than simply answering questions, MythBuster AI teaches users how to evaluate information, understand evidence, and make informed decisions in a world increasingly shaped by AI-generated content and rapidly spreading misinformation.
