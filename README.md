# Hierarchical Reasoning Agent

A professional AI-powered platform designed to break down complex problems into structured layers for comprehensive analysis and intelligent solutions.
Deployed live at: **[https://hierarchical-reasoning-agent.vercel.app/](https://hierarchical-reasoning-agent.vercel.app/)**

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Example Use Cases](#example-use-cases)
5. [Tech Stack](#tech-stack)
6. [Installation](#installation)
7. [Environment Variables](#environment-variables)
8. [Usage](#usage)
9. [Project Structure](#project-structure)
10. [Deployment](#deployment)
11. [License](#license)

---

## Overview

The **Hierarchical Reasoning Agent** is built to help users tackle complex, multi-dimensional problems by decomposing them into manageable layers of reasoning.
It uses **Large Language Models (LLMs)** from Groq to analyze queries, generate structured responses, and deliver actionable insights across domains such as legal strategy, business planning, data science, healthcare, finance, and marketing.

---

## Features

* **Multi-Domain Reasoning** – Handles queries from legal, business, healthcare, AI, finance, and more.
* **Hierarchical Analysis** – Breaks down broad problems into structured, logical steps.
* **Groq LLM Integration** – Uses high-performance inference for fast, accurate responses.
* **Customizable Prompts** – Extend or modify reasoning guidelines via `Prompt-Example.txt`.
* **Streamlit Interface** – Interactive web-based UI for real-time input and output.
* **Structured Output** – Responses formatted for clarity using custom output formatting.
* **Environment-Based Configuration** – Secure API key handling through `.env`.

---

## How It Works

1. **User Input** – The user provides a query or problem statement through the UI.
2. **Prompt Structuring** – The system uses domain-specific prompt templates from `Prompt-Example.txt` to guide reasoning.
3. **Hierarchical Reasoning** – The agent decomposes the problem into layers:

   * **High-level strategy**
   * **Mid-level components**
   * **Detailed action steps**
4. **LLM Execution** – The request is sent to Groq's API for fast model inference.
5. **Formatted Output** – The result is structured by `output_formatter.py` for easy interpretation.

---

## Example Use Cases

From the included `Prompt-Example.txt`:

**Legal & Compliance**

* Defend a startup accused of trademark infringement by proving prior use.
* Build a defense for breach of contract by highlighting ambiguous terms.

**Business & Consulting**

* Market entry strategy for a fintech startup in Southeast Asia.
* Customer retention strategy for a SaaS company with high churn.

**Data Science & AI**

* Fraud detection model for financial services.
* AI recommendation system for OTT platforms.

**Healthcare & Biotech**

* AI diagnostics system for early disease detection.
* Clinical trial recruitment strategy.

**Finance & Investment**

* Investment strategy in volatile markets.
* Budget optimization for nonprofits.

**Marketing & Consumer Insights**

* Digital marketing campaigns to boost lead generation.
* Influencer partnership strategies.

---

## Tech Stack

* **Frontend/UI**: [Streamlit](https://streamlit.io/)
* **Backend**: Python
* **LLM Provider**: [Groq](https://groq.com/)
* **Environment Management**: `python-dotenv`
* **Console Logging**: `rich`

**Requirements** (from `requirements.txt`):

```txt
groq
python-dotenv
rich
streamlit
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/hierarchical-reasoning-agent.git
cd hierarchical-reasoning-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get your Groq API key from [Groq’s developer portal](https://groq.com/).

---

## Usage

### Local Run

```bash
streamlit run ui.py
```

This will open the application in your browser at `http://localhost:8501`.

### Input

* Enter a problem statement.
* Select or provide a domain-specific prompt.
* Submit to receive a hierarchical breakdown.

---

## Project Structure

```
.
├── agent.py                # Core hierarchical reasoning logic
├── groq_client.py          # Groq API client wrapper
├── main.py                 # Entry point for CLI or backend execution
├── output_formatter.py     # Output formatting logic
├── ui.py                   # Streamlit web interface
├── Prompt-Example.txt      # Sample prompts for multiple domains
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── LICENSE                 # License information
```

---

## Deployment

The project is deployed on **Vercel** at:
[https://hierarchical-reasoning-agent.vercel.app/](https://hierarchical-reasoning-agent.vercel.app/)

To deploy your own:

1. Push the repository to GitHub.
2. Link the repository to your [Vercel](https://vercel.com/) account.
3. Set `GROQ_API_KEY` in Vercel’s Environment Variables.
4. Deploy and access via your Vercel-generated URL.

---

## License

This project is licensed under the [MIT License](LICENSE).