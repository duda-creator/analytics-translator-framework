"""Tools shared across specialist agents. Mirrors the twin project's
lead-capture / unanswered-question pattern, but with Pydantic-validated
arguments and the Agents SDK's function_tool decorator instead of a manual
JSON-schema + if/elif dispatch.
"""

import os
from typing import Literal

import httpx
from agents import function_tool

from models import LeadCapture, Route, UnansweredQuestion

PUSHOVER_URL = "https://api.pushover.net/1/messages.json"


def _pushover_notify(title: str, message: str) -> None:
    token = os.getenv("PUSHOVER_TOKEN")
    user = os.getenv("PUSHOVER_USER")
    if not token or not user:
        print(f"[pushover:disabled] {title}\n{message}")
        return
    try:
        httpx.post(
            PUSHOVER_URL,
            data={"token": token, "user": user, "title": title, "message": message},
            timeout=10,
        )
    except httpx.HTTPError as exc:
        print(f"[pushover:error] {exc}\n{title}\n{message}")


@function_tool
def capture_lead(
    use_case_summary: str,
    name: str | None = None,
    email: str | None = None,
    company: str | None = None,
    urgency: str = "medium",
) -> str:
    """Record a prospective lead and notify Marcin. Call this whenever the
    user shares contact info (name/email/company) or asks how to engage,
    book a call, or get started.

    Args:
        use_case_summary: One or two sentences summarising the user's business problem.
        name: The user's name, if given.
        email: The user's email, if given.
        company: The user's company, if given.
        urgency: One of "low", "medium", "high" based on how time-sensitive the user's need sounds.
    """
    lead = LeadCapture(
        name=name,
        email=email,
        company=company,
        use_case_summary=use_case_summary,
        urgency=urgency,
        source_agent="use_case",
    )
    _pushover_notify(
        "New AI Advisor lead",
        f"Name: {lead.name or 'n/a'}\nEmail: {lead.email or 'n/a'}\n"
        f"Company: {lead.company or 'n/a'}\nUrgency: {lead.urgency.value}\n"
        f"Use case: {lead.use_case_summary}",
    )
    return "Lead recorded. Thank the user and let them know Marcin will follow up."


@function_tool
def record_unanswered_question(
    question: str,
    route_attempted: Literal["background", "framework", "use_case", "general"],
    notes: str | None = None,
) -> str:
    """Record a question the advisor couldn't confidently answer from its
    knowledge base, so Marcin can review gaps.

    Args:
        question: The user's original question, verbatim or close to it.
        route_attempted: Which specialist tried to answer it.
        notes: Any extra context about why it couldn't be answered.
    """
    record = UnansweredQuestion(question=question, route_attempted=Route(route_attempted), notes=notes)
    _pushover_notify(
        "AI Advisor knowledge gap",
        f"Route: {record.route_attempted.value}\nQuestion: {record.question}\nNotes: {record.notes or 'n/a'}",
    )
    return "Noted for review. Answer honestly that you don't have that information yet."
