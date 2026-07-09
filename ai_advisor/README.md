---
title: Marcin Duda AI Advisor
emoji: 🧭
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: "6.20.0"
app_file: app.py
pinned: false
---

# AI Advisor — Marcin Duda, Analytics Translator

Interactive advisor for the [Last-Mile Analytics Delivery Framework](https://github.com/duda-creator/analytics-translator-framework). Ask about Marcin's background, the Delivery Framework itself, or describe a business problem to get a structured diagnostic mapping it to a framework stage, artefact set, and engagement type.

Built as a code-orchestrated multi-agent system (OpenAI Agents SDK): a router classifies each turn, then dispatches to a Background, Framework, or Use-Case specialist agent, each returning a typed (Pydantic) structured output.

## Local development

```bash
pip install -r requirements-dev.txt
cp .env.example .env   # fill in OPENAI_API_KEY at minimum
python scripts/build_knowledge.py   # only needed if source docs changed
python app.py
```
