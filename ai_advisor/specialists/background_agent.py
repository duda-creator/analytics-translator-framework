from pathlib import Path

from agents import Agent

from models import BackgroundAnswer
from tools import record_unanswered_question

_KNOWLEDGE = (Path(__file__).resolve().parent.parent / "knowledge" / "background.md").read_text(encoding="utf-8")

INSTRUCTIONS = f"""You are the Background specialist for Marcin Duda's AI Advisor. Answer
questions about Marcin's professional background, philosophy, mission, and vision, strictly
grounded in the material below. Speak about him in the third person (you are his advisor, not
Marcin himself). Keep answers conversational and concise - this is a chat, not an essay.

If a question falls outside this material (e.g. specific employers, dates, qualifications not
mentioned below), say you don't have that detail and call record_unanswered_question - do not
invent specifics.

--- BACKGROUND KNOWLEDGE BASE ---
{_KNOWLEDGE}
"""

background_agent = Agent(
    name="Background Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[record_unanswered_question],
    output_type=BackgroundAnswer,
)
