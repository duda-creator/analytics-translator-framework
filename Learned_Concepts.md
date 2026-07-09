# Learned Concepts

This file consolidates key techniques, frameworks, and design patterns from:
- 1_foundations
- 2_openai

It also includes a focused comparison of the two main projects:
- 1_foundations/twin
- 2_openai/deep_research

Community contribution folders are excluded.

## High-Level Conceptual Frameworks

### Prompt Chaining and Decomposition
- Multi-step prompting is used to break ambiguous tasks into staged reasoning flows.
- Example pattern: identify business area -> identify pain point -> propose agentic solution.
- Reference: [1_foundations/1_lab1.ipynb](1_foundations/1_lab1.ipynb#L527), [1_foundations/1_lab1.ipynb](1_foundations/1_lab1.ipynb#L528), [1_foundations/1_lab1.ipynb](1_foundations/1_lab1.ipynb#L529)

### Orchestrator-Workers and LLM-as-Judge
- Multiple model outputs are generated, then a separate model evaluates/ranks candidates.
- Judging often uses strict JSON output contracts for machine readability.
- Reference: [1_foundations/2_lab2.ipynb](1_foundations/2_lab2.ipynb#L735), [1_foundations/2_lab2.ipynb](1_foundations/2_lab2.ipynb#L748), [1_foundations/2_lab2.ipynb](1_foundations/2_lab2.ipynb#L847)

### Agent Loop Fundamentals
- Core loop pattern: model call -> detect tool calls -> execute tool(s) -> append tool results -> repeat until final text output.
- This is demonstrated explicitly before abstraction into frameworks.
- Reference: [1_foundations/3_lab3.ipynb](1_foundations/3_lab3.ipynb#L1117), [1_foundations/3_lab3.ipynb](1_foundations/3_lab3.ipynb#L1238), [1_foundations/3_lab3.ipynb](1_foundations/3_lab3.ipynb#L1241)

### Tool Calling as a Control Plane
- Tools are represented as JSON function schemas plus runtime dispatch logic.
- Two practical dispatch styles appear:
- Manual conditional routing (if/elif by tool name).
- Generic map-based routing (tool name -> callable).
- Reference: [1_foundations/4_lab4.ipynb](1_foundations/4_lab4.ipynb#L247), [1_foundations/4_lab4.ipynb](1_foundations/4_lab4.ipynb#L311), [1_foundations/twin/tools.py](1_foundations/twin/tools.py#L99)

### Safety and Reliability Behaviors
- Unknown-answer capture replaces hallucination-prone behavior.
- Guardrail logic appears both as explicit control checks and framework-integrated guardrails.
- Reference: [1_foundations/4_lab4.ipynb](1_foundations/4_lab4.ipynb#L377), [2_openai/3_lab3.ipynb](2_openai/3_lab3.ipynb#L502), [2_openai/3_lab3.ipynb](2_openai/3_lab3.ipynb#L537)

### Structured Outputs and Typed Contracts
- Pydantic models are used to define output schemas for typed downstream processing.
- SDK output_type mappings reduce post-processing ambiguity.
- Reference: [2_openai/3_lab3.ipynb](2_openai/3_lab3.ipynb#L354), [2_openai/3_lab3.ipynb](2_openai/3_lab3.ipynb#L416), [2_openai/4_lab4.ipynb](2_openai/4_lab4.ipynb#L215), [2_openai/deep_research/writer_agent.py](2_openai/deep_research/writer_agent.py#L16)

### Memory, Sessions, and State
- Conversation state is handled both manually (message history) and through SDK sessions.
- SQLite-backed sessions support persistent conversational memory.
- Reference: [2_openai/1_lab1.ipynb](2_openai/1_lab1.ipynb#L529), [2_openai/1_lab1.ipynb](2_openai/1_lab1.ipynb#L644)

### Observability and Tracing
- Trace wrappers and trace IDs are used to debug orchestration behavior and tool execution.
- Reference: [2_openai/1_lab1.ipynb](2_openai/1_lab1.ipynb#L194), [2_openai/2_lab2.ipynb](2_openai/2_lab2.ipynb#L504), [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L12)

### Parallelization for Throughput
- Async fan-out with gather is used for concurrent worker execution.
- Appears in both lab workflows and full project pipelines.
- Reference: [2_openai/2_lab2.ipynb](2_openai/2_lab2.ipynb#L505), [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L29)

## Focus Project: twin

### Core Architecture
- First-principles digital twin chatbot built with OpenAI Chat Completions plus Gradio.
- Manual agent loop with explicit tool protocol.
- Reference: [1_foundations/twin/app.py](1_foundations/twin/app.py#L1), [1_foundations/twin/app.py](1_foundations/twin/app.py#L18)

### Grounding and Persona Control
- System prompt is grounded using local profile documents.
- Persona constraints enforce professional scope and reduce off-domain drift.
- Reference: [1_foundations/twin/context.py](1_foundations/twin/context.py#L1), [1_foundations/twin/context.py](1_foundations/twin/context.py#L17)

### Tooling and Side Effects
- Tools capture leads, unanswered questions, and consulting entry-point questions.
- Notifications are pushed through Pushover for operational follow-up.
- Reference: [1_foundations/twin/tools.py](1_foundations/twin/tools.py#L15), [1_foundations/twin/tools.py](1_foundations/twin/tools.py#L47), [1_foundations/twin/tools.py](1_foundations/twin/tools.py#L99)

### Practical Pattern
- Best viewed as a transparency-first implementation of agent mechanics.
- Strong for learning protocol internals and debugging tool behavior.

## Focus Project: deep_research

### Core Architecture
- Multi-agent pipeline built on OpenAI Agents SDK.
- Manager orchestrates planner -> search workers -> writer -> email sender.
- Reference: [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L11), [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L16)

### Specialized Agent Roles
- Planner Agent outputs typed search plans.
- Search Agent enforces web search tool usage.
- Writer Agent outputs typed report objects.
- Email Agent converts report into deliverable communication.
- Reference: [2_openai/deep_research/planner_agent.py](2_openai/deep_research/planner_agent.py#L22), [2_openai/deep_research/search_agent.py](2_openai/deep_research/search_agent.py#L12), [2_openai/deep_research/writer_agent.py](2_openai/deep_research/writer_agent.py#L22), [2_openai/deep_research/email_agent.py](2_openai/deep_research/email_agent.py#L35)

### Concurrency and Streaming UX
- Search tasks execute concurrently via asyncio.gather.
- User-facing UI streams status updates and final report text progressively.
- Reference: [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L29), [2_openai/deep_research/app.py](2_openai/deep_research/app.py#L9)

### Typed Contracts and Reliability
- Pydantic output models provide stable handoffs between stages.
- Model settings enforce required tool behavior where determinism matters.
- Reference: [2_openai/deep_research/planner_agent.py](2_openai/deep_research/planner_agent.py#L14), [2_openai/deep_research/writer_agent.py](2_openai/deep_research/writer_agent.py#L16), [2_openai/deep_research/email_agent.py](2_openai/deep_research/email_agent.py#L12)

## twin vs deep_research: Conceptual Comparison

### Control Style
- twin: explicit, manual loop and tool protocol.
- deep_research: framework-managed orchestration with role-specialized agents.

### Main Objective
- twin: persona-faithful conversational representation with selective side effects.
- deep_research: reproducible research workflow that generates and delivers a structured report.

### Data Contracts
- twin: primarily text responses plus lightweight tool argument schemas.
- deep_research: typed structured outputs (plans and reports) as first-class workflow contracts.

### Operational Maturity Pattern
- twin: ideal for learning and transparent debugging of agent internals.
- deep_research: closer to production workflow architecture with observability, parallelization, and typed stage boundaries.

## Primary Frameworks and Libraries Used
- OpenAI Chat Completions API: [1_foundations/twin/app.py](1_foundations/twin/app.py#L1)
- OpenAI Agents SDK: [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L1)
- Pydantic: [2_openai/deep_research/planner_agent.py](2_openai/deep_research/planner_agent.py#L1)
- Gradio: [1_foundations/twin/app.py](1_foundations/twin/app.py#L5), [2_openai/deep_research/app.py](2_openai/deep_research/app.py#L1)
- Dotenv: [1_foundations/twin/app.py](1_foundations/twin/app.py#L5), [2_openai/deep_research/app.py](2_openai/deep_research/app.py#L3)
- Asyncio: [2_openai/deep_research/research_manager.py](2_openai/deep_research/research_manager.py#L6)

## Short Takeaway
- The learning arc moves from manual agent mechanics toward framework-based multi-agent systems.
- twin teaches how the loop works under the hood.
- deep_research demonstrates how to scale that loop into a typed, observable, parallelized pipeline.
