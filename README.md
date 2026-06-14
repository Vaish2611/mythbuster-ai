# 🧱 MythBuster AI

## Break Myths. Build Truth.

MythBuster AI is an AI-powered misinformation detection and fact verification platform designed to help users evaluate the credibility of claims using evidence-based reasoning and trusted sources.

The platform combines a FastAPI backend with a LEGO-themed Next.js frontend to provide transparent fact verification through:

* Evidence-backed verdicts
* Trust scoring
* Source reliability analysis
* Explainable reasoning
* Source transparency

Rather than simply labeling claims as true or false, MythBuster AI helps users understand why a claim is credible or misleading.

---

# 🎯 Problem Statement

The internet is flooded with misinformation.

Users regularly encounter claims such as:

* Vaccines cause autism
* Antibiotics work against viral infections
* Smoking does not cause cancer
* F-1 students cannot apply for OPT
* STEM graduates do not qualify for OPT extensions

Traditional search engines provide thousands of results, forcing users to determine which information is trustworthy.

Most fact-checking tools only provide a verdict without explaining:

* Why the claim is true or false
* How reliable the sources are
* How much evidence supports the verdict
* How misinformation spreads

MythBuster AI addresses this challenge through transparent, evidence-based verification.

---

# 🚀 Solution

MythBuster AI follows a structured verification workflow:

User Claim
↓
Claim Analysis
↓
Evidence Retrieval
↓
Source Credibility Evaluation
↓
Trust Scoring
↓
Verdict Generation
↓
Transparent Explanation

The platform currently supports:

### 🏥 Healthcare Verification

and

### 🛂 Immigration & Visa Verification

with future expansion planned for additional domains.

---

# ✨ Current Features

## ✅ Claim Verification

Users can enter a claim such as:

> Vaccines cause autism

The system returns:

* Verdict
* Confidence score
* Explanation
* Supporting evidence
* Source reliability
* Truth score

---

## ✅ Evidence Retrieval

The system retrieves verified evidence from trusted sources.

Current sources include:

### Healthcare

* CDC
* WHO

### Immigration

* USCIS

Each source is assigned a credibility score.

Example:

Source: CDC

Credibility: 99/100

---

## ✅ Trust Dashboard

Every claim receives three trust metrics:

### 🧱 Truth Score

Measures how strongly the available evidence supports or contradicts a claim.

### 🔍 Evidence Strength Score

Measures the quality and quantity of evidence available.

### 🏛️ Source Reliability Score

Measures the credibility of the organizations providing evidence.

---

## ✅ Source Transparency

Users can inspect:

* Source Name
* Supporting Fact
* Credibility Score
* Direct Source Link

This allows users to independently verify information.

---

## ✅ Explainable Results

Instead of returning only a verdict, MythBuster AI provides:

* Explanation
* Supporting evidence
* Confidence level
* Source information

making the decision process transparent.

---

## ✅ LEGO-Themed User Interface

The frontend is built around a LEGO-inspired design system featuring:

* LEGO cards
* LEGO trust dashboard
* LEGO score blocks
* LEGO source cards
* Interactive visual layout

The design emphasizes accessibility and engagement.

---

# 📚 Current Domain Coverage

MythBuster AI currently focuses on two specialized domains.

---

## 🏥 Healthcare Verification

Knowledge base examples:

### Vaccines cause autism

Verdict:

FALSE

Source:

CDC

---

### COVID vaccines are effective

Verdict:

TRUE

Source:

WHO

---

### Antibiotics work against viral infections

Verdict:

FALSE

Source:

WHO

---

### Smoking causes cancer

Verdict:

TRUE

Source:

WHO

---

### High blood pressure is dangerous

Verdict:

TRUE

Source:

WHO

---

## 🛂 Immigration & Visa Verification

Knowledge base examples:

### F-1 students may apply for OPT

Verdict:

TRUE

Source:

USCIS

---

### STEM graduates qualify for a 24-month OPT extension

Verdict:

TRUE

Source:

USCIS

---

### H-1B petitions require filing fees

Verdict:

TRUE

Source:

USCIS

---

### Green card applicants may adjust status within the United States

Verdict:

TRUE

Source:

USCIS

---

# 🏗️ Architecture

## Frontend

Next.js + React

Responsibilities:

* User interaction
* Claim submission
* Result visualization
* LEGO trust dashboard

---

## Backend

FastAPI

Responsibilities:

* Claim processing
* Knowledge base search
* Evidence retrieval
* Score calculation
* Verdict generation

---

## Knowledge Base

Curated repository of verified facts.

Current domains:

* Healthcare
* Immigration

Future domains:

* Finance
* Education
* Technology
* Public Policy

---

# 🧠 Trust Scoring System

The system calculates:

Truth Score =
50% Confidence Score +
30% Evidence Strength +
20% Source Reliability

This provides a transparent credibility framework.

---

# 🛠️ Technology Stack

## Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

---

## Backend

* FastAPI
* Python
* Uvicorn

---

## Data Layer

* Structured Knowledge Base
* Source Credibility Repository

---

## Future AI Layer

Planned:

* Azure AI Foundry
* Azure AI Agents
* Azure OpenAI
* Semantic Kernel
* Retrieval-Augmented Generation (RAG)

---

# 📊 Example Workflow

User Input:

> Vaccines cause autism

System Process:

1. Analyze claim
2. Search knowledge base
3. Retrieve CDC evidence
4. Calculate trust scores
5. Generate verdict

Output:

Verdict: FALSE

Truth Score: 99

Evidence Strength: 99

Source Reliability: 99

Supporting Source:

CDC

---

# 🚧 Features Under Development

The following capabilities are actively being developed.

## Myth Origin Tracing

Investigates:

* Where a myth originated
* How it spread
* Major amplification points

Status:

🚧 Work In Progress

---

## Multi-Agent Verification Pipeline

Planned agents:

* Claim Extraction Agent
* Evidence Retrieval Agent
* Verification Agent
* Bias Detection Agent
* Counter-Perspective Agent
* Explainability Agent

Status:

🚧 Work In Progress

---

## Bias Detection

Will identify:

* Confirmation bias
* Emotional framing
* Cherry-picked statistics
* Misleading correlations

Status:

🚧 Work In Progress

---

## Counter-Perspective Generation

Will provide:

* Opposing viewpoints
* Areas of uncertainty
* Balanced interpretations

Status:

🚧 Work In Progress

---

# 🗺️ Future Roadmap

### Phase 1

Healthcare Verification

✅ Complete

### Phase 2

Immigration Verification

✅ Complete

### Phase 3

LLM-Powered Fact Verification

🚧 In Progress

### Phase 4

Myth Origin Tracing

🚧 In Progress

### Phase 5

Finance & Investment Verification

🔮 Planned

### Phase 6

Technology & AI Misinformation

🔮 Planned

### Phase 7

Educational & Career Guidance Verification

🔮 Planned

### Phase 8

Multilingual Verification Support

🔮 Planned

---

# 🌍 Vision

Our vision is to build an explainable AI-powered truth ecosystem that helps people navigate the modern information landscape through transparent evidence, trusted sources, and critical thinking.

Rather than simply answering whether a claim is true or false, MythBuster AI aims to teach users how to evaluate information, understand evidence, and make informed decisions in a world increasingly shaped by misinformation.
