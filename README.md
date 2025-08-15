# Hierarchical Reasoning Agent

A professional AI-powered platform designed to break down complex problems into structured layers for comprehensive analysis and intelligent solutions.
Deployed live at: **[https://hierarchical-reasoning-agent.vercel.app/](https://hierarchical-reasoning-agent.vercel.app/)**

---

## Table of Contents

1. [Overview](#overview)
2. [Why This Is Different](#why-this-is-different)
3. [Real-World Business Impact](#real-world-business-impact)
4. [Features](#features)
5. [How It Works](#how-it-works)
6. [Example Use Cases](#example-use-cases)
7. [Tech Stack](#tech-stack)
8. [Installation](#installation)
9. [Environment Variables](#environment-variables)
10. [Usage](#usage)
11. [Project Structure](#project-structure)
12. [Deployment](#deployment)
13. [License](#license)

---

## Overview

The **Hierarchical Reasoning Agent** is built to help users tackle complex, multi-dimensional problems by decomposing them into manageable layers of reasoning.
It uses **Large Language Models (LLMs)** from Groq to analyze queries, generate structured responses, and deliver actionable insights across domains such as legal strategy, business planning, data science, healthcare, finance, and marketing.

---

## Why This Is Different

While advanced AI models like Claude Opus 4.1 or ChatGPT-5 can produce impressive single-pass answers, they often deliver **long, unstructured outputs** that can be hard to validate, adapt, or integrate into workflows.

**Hierarchical Reasoning Agent** stands out by:

* **Layered Problem Decomposition** – Every query is broken into high-level strategy, mid-level components, and detailed action steps, giving you clarity and traceability.
* **Domain-Specific Prompt Library** – Preloaded prompts for legal, business, finance, healthcare, data science, and more, saving time on prompt engineering.
* **Consistent Structured Output** – Uses a dedicated formatter so responses follow the same predictable structure, making review, storage, and reuse straightforward.
* **High-Speed Inference** – Powered by Groq’s ultra-low-latency LLM API, enabling near-instant reasoning for complex problems.
* **Human-in-the-Loop Ready** – Outputs are optimized for team review and refinement, not just “one-shot” answers.

This isn’t just AI that answers — it’s AI that **thinks with you**, structures your strategy, and produces outputs you can directly act on.

---

## Real-World Business Impact

* **Accelerates Decision-Making** – Reduces hours or days of manual analysis into structured, reviewable steps in minutes.
* **Improves Accuracy & Accountability** – Layered reasoning makes it easier to verify each decision point and avoid blind trust in AI.
* **Cuts Analysis Costs** – Teams can reuse structured outputs across reports, client deliverables, and strategies.
* **Bridges Strategy & Execution** – Transforms vague, high-level goals into concrete, actionable plans.

**Example:**
A consulting firm can input “Enter the Southeast Asian fintech market” and receive a structured plan with regulatory considerations, competitor analysis, resource requirements, and phased execution steps — ready for client presentation.

---

## Features

* **Multi-Domain Reasoning** – Handles queries across industries and problem types.
* **Hierarchical Analysis** – Clear breakdown into strategies, components, and actions.
* **Groq LLM Integration** – Fast, reliable inference for minimal wait times.
* **Customizable Prompts** – Extend reasoning with domain-specific templates in `Prompt-Example.txt`.
* **Streamlit Interface** – Simple, interactive UI for real-time reasoning.
* **Structured Output** – Predictable, reusable formats.

---

## How It Works

1. **User Input** – Provide a problem statement in the UI.
2. **Prompt Structuring** – Templates guide reasoning by domain.
3. **Hierarchical Breakdown** – Strategy → Components → Action Steps.
4. **LLM Execution** – Groq API delivers structured reasoning.
5. **Formatted Output** – `output_formatter.py` organizes results.

---

## Example Use Cases

From `Prompt-Example.txt`:

* **Legal & Compliance** – Trademark defense, contract dispute strategies.
* **Business & Consulting** – Market entry plans, turnaround strategies.
* **Data Science & AI** – Fraud detection, recommendation systems.
* **Healthcare** – AI diagnostics, clinical trial recruitment.
* **Finance** – Investment strategies, risk mitigation.
* **Marketing** – Campaign design, influencer partnerships.

---

## Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **LLM Provider**: Groq
* **Env Management**: python-dotenv
* **Console Logging**: rich

**Requirements**:

```txt
groq
python-dotenv
rich
streamlit
```

---

## Installation

```bash
git clone https://github.com/<your-username>/hierarchical-reasoning-agent.git
cd hierarchical-reasoning-agent
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` in the root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

```bash
streamlit run ui.py
```

Visit `http://localhost:8501`.

---

## Project Structure

```
.
├── agent.py
├── groq_client.py
├── main.py
├── output_formatter.py
├── ui.py
├── Prompt-Example.txt
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Deployment

Deployed on Vercel:
[https://hierarchical-reasoning-agent.vercel.app/](https://hierarchical-reasoning-agent.vercel.app/)

To deploy your own:

1. Push to GitHub.
2. Link to Vercel.
3. Set `GROQ_API_KEY` in Vercel env variables.
4. Deploy.

---

## License

This project is licensed under the [MIT License](LICENSE).