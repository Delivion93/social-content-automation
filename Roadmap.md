# Social Content Agents - Development Roadmap

## Phase 1 — Project Setup

Goal: Create the foundation of the project.

Tasks:

* Create Git repository
* Define project structure
* Configure virtual environment
* Install dependencies
* Configure LLM provider (OpenAI/Ollama)
* Create Pydantic schemas

Deliverable:

* Running project with basic LLM communication

---

## Phase 2 — Content Strategist Agent

Goal: Generate marketing concepts.

Input:

* Product/service
* Target audience
* Brand description

Output:

* Campaign idea
* Content concept
* Tone of voice

Workflow:

User
↓
Strategist Agent
↓
Campaign Concept

Deliverable:

* First working AI agent

---

## Phase 3 — Copywriter Agent

Goal: Generate social media posts.

Input:

* Campaign Concept

Output:

* Instagram post
* Facebook post
* LinkedIn post

Workflow:

Campaign Concept
↓
Copywriter Agent
↓
Social Media Posts

Deliverable:

* Complete content generation

---

## Phase 4 — Compliance Agent

Goal: Validate generated content.

Checks:

* Brand tone
* Required keywords
* Restricted words
* Content completeness

Workflow:

Posts
↓
Compliance Agent
↓
Approval Report

Deliverable:

* Multi-agent workflow

---

## Phase 5 — Agent Orchestration

Goal: Connect all agents together.

Workflow:

User Request
↓
Strategist Agent
↓
Copywriter Agent
↓
Compliance Agent
↓
Final Response

Deliverable:

* End-to-end pipeline

---

## Phase 6 — FastAPI Integration

Goal: Expose the workflow as an API.

Endpoints:

POST /generate-content

Request:
{
"product": "...",
"audience": "...",
"brand": "..."
}

Response:
{
"concept": "...",
"posts": {...},
"validation": {...}
}

Deliverable:

* Backend service

---

## Phase 7 (Optional) — Image Prompt Designer

Goal: Generate prompts for image creation.

Input:

* Campaign Concept

Output:

* Stable Diffusion prompt
* DALL-E prompt

Workflow:

Campaign Concept
↓
Prompt Designer
↓
Image Prompt

Deliverable:

* AI image prompt generation

---

## Phase 8 (Optional) — Image Generation

Goal: Generate actual images.

Workflow:

Image Prompt
↓
Image Model
↓
Marketing Image

Deliverable:

* Complete content package

---

# Final Architecture


                 ┌──────────────────┐
                 │ User Request     │
                 └─────────┬────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Strategist Agent   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Copywriter Agent   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Compliance Agent   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Final Content      │
                └────────────────────┘


Optional Extension:

Strategist Agent
│
▼
Prompt Designer
│
▼
Image Generation
