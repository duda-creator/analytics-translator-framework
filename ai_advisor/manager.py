"""Code-orchestrated manager: classify -> dispatch -> format.

Mirrors the deep_research project's research_manager.py pattern (explicit
Python control flow calling typed-output Agents via Runner.run) rather than
the Agents SDK's native handoffs.
"""

from agents import Runner

from models import BackgroundAnswer, FrameworkAnswer, Route, UseCaseDiagnostic
from specialists.background_agent import background_agent
from specialists.framework_agent import framework_agent
from specialists.router_agent import router_agent
from specialists.use_case_agent import use_case_agent

_AGENTS = {
    Route.BACKGROUND: background_agent,
    Route.FRAMEWORK: framework_agent,
    Route.USE_CASE: use_case_agent,
}

_GENERAL_REPLY = (
    "Hi, I'm Marcin's AI Advisor. Ask me about his background and philosophy, "
    "how the Delivery Framework works, or describe a business problem you're "
    "facing and I'll map it to the framework for you."
)

_FALLBACK_REPLY = (
    "Sorry, I hit a snag answering that. Could you try rephrasing, "
    "or ask something else about Marcin, the framework, or your use case?"
)

_HISTORY_TURNS = 8


class AdvisorManager:
    async def run_turn(self, message: str, history: list[dict]) -> str:
        conversation = self._build_conversation(message, history)

        try:
            route_result = await Runner.run(router_agent, conversation)
            route_decision = route_result.final_output
        except Exception as exc:
            print(f"[manager] routing failed: {exc}")
            return _FALLBACK_REPLY

        if route_decision.route == Route.GENERAL:
            return _GENERAL_REPLY

        agent = _AGENTS[route_decision.route]
        try:
            result = await Runner.run(agent, conversation)
        except Exception as exc:
            print(f"[manager] specialist '{agent.name}' failed: {exc}")
            return _FALLBACK_REPLY

        return self._format_output(result.final_output)

    def _build_conversation(self, message: str, history: list[dict]) -> list[dict]:
        turns = [{"role": h["role"], "content": h["content"]} for h in history[-_HISTORY_TURNS:]]
        turns.append({"role": "user", "content": message})
        return turns

    def _format_output(self, output) -> str:
        if isinstance(output, UseCaseDiagnostic):
            return self._format_use_case(output)
        if isinstance(output, (FrameworkAnswer, BackgroundAnswer)):
            return self._format_answer(output)
        return str(output)

    def _format_use_case(self, diagnostic: UseCaseDiagnostic) -> str:
        lines = [
            f"**Business area:** {diagnostic.business_area}",
            f"**What's going on:** {diagnostic.pain_point_summary}",
        ]
        if diagnostic.matched_entry_point:
            lines.append(f"**Closest fit:** {diagnostic.matched_entry_point}")
        lines.append(f"**Recommended starting stage:** {diagnostic.recommended_stage.value}")
        if diagnostic.recommended_artefacts:
            artefacts = "\n".join(f"- {a}" for a in diagnostic.recommended_artefacts)
            lines.append(f"**Relevant artefacts:**\n{artefacts}")
        lines.append(f"**Suggested engagement:** {diagnostic.engagement_type.value}")
        lines.append(f"\n*{diagnostic.reasoning}*")
        return "\n\n".join(lines)

    def _format_answer(self, answer) -> str:
        parts = [answer.answer_markdown]
        related_artefacts = getattr(answer, "related_artefacts", None)
        related_stage = getattr(answer, "related_stage", None)
        if related_stage or related_artefacts:
            bits = []
            if related_stage:
                bits.append(f"stage: {related_stage}")
            if related_artefacts:
                bits.append(f"artefacts: {', '.join(related_artefacts)}")
            parts.append(f"\n_({'; '.join(bits)})_")
        if answer.follow_up_prompt:
            parts.append(f"\n{answer.follow_up_prompt}")
        return "\n".join(parts)
