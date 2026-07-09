import gradio as gr
from dotenv import load_dotenv

from manager import AdvisorManager

load_dotenv()
manager = AdvisorManager()


async def respond(message: str, history: list[dict]) -> str:
    return await manager.run_turn(message, history)


demo = gr.ChatInterface(
    fn=respond,
    title="AI Advisor — Marcin Duda, Analytics Translator",
    description=(
        "Ask about Marcin's background, how the Delivery Framework works, "
        "or describe a business problem for a diagnostic."
    ),
    examples=[
        "What's the Delivery Framework?",
        "Tell me about Marcin's background and philosophy.",
        "We have three spreadsheets nobody trusts and our board meeting is Monday.",
    ],
)

if __name__ == "__main__":
    demo.launch()
