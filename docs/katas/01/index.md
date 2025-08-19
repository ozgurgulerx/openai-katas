---
title: 01 · Responses API — Simple Text
---
<script>window.recordKataVisit && window.recordKataVisit('01-tokens-and-temp');</script>

# 01 · Responses API — Simple Text Generation
**Time:** 10–15m · **Level:** Intro · **Tags:** API, Responses, Text  
[:octicons-codespaces-16: Open Codespace in this kata](https://github.com/codespaces/new/ozgurgulerx/openai-katas?quickstart=1#folder=/katas/01-tokens-and-temp)

=== "Markdown question"
    ## Primer
    - The Responses API is OpenAI’s unified, tool-native endpoint for text and more.
    - For simple text: call `/v1/responses` with a `model` and `input` prompt.
    - Prefer Responses over legacy Completions/Chat Completions for new work.

    ## Your task
    1. Implement `run_prompt(prompt: str, model: str = "gpt-4o-mini") -> str` using the Responses API.
    2. Send a single short prompt and print the returned text.
    3. Keep it simple: text-only (no tools, no structured outputs yet).

    ## Run & verify
    ```bash
    python docs/katas/01/question.py
    ```

=== "Notebook question"
    Open the notebook version: **[question.ipynb](question.ipynb)**

--- 

## About the Responses API (Aug 2025)

### TL;DR
- **Unified, tool-native, multimodal, agentic endpoint.**
- Orchestrates tools (web/file search, Code Interpreter, image gen, MCP servers), strict structured outputs, typed streaming, background jobs, and reasoning lifecycle.
- Completions = legacy; Chat Completions = fine for plain chat; most new agentic features land in Responses.

### What it is (essentials)
- Single endpoint: `/v1/responses` accepting text + images, optional instructions, and a tools array.
- Models can call tools mid-reasoning (incl. remote MCP servers); emits semantic stream events for precise UIs.
- First-class Structured Outputs: JSON Schema with `strict: true` guarantees schema-valid results.
- Background mode for long tasks (poll/webhook) — great for deep research, bigger code/RAG.
- Reasoning upgrades (o‑series/4.1/4o), with encrypted reasoning items (enterprise).

### Why OpenAI recommends it
- Core API primitive for agentic apps; new capabilities ship here first.
- Collapses multiple APIs into one coherent surface → less glue code, lower integration risk.

### How it differs from Completions / Chat Completions
- Programming model:
  - Completions: prompt → text; no native tools; minimal structure.
  - Chat Completions: messages array; add‑on tool calling; simple chats.
  - Responses: input + instructions + tools + structured outputs + background + typed streaming events.
- Tooling: Built‑in tools (web search, file search/RAG, Code Interpreter, image gen/edit, computer use where available) and remote MCP servers.
- Outputs: Strict schemas (`response_format.json_schema` or function args with `strict:true`) vs. best‑effort JSON.
- Runtime & streaming: Semantic events (`response.created`, `output_text.delta`, `tool_call.*`, …) vs. raw token deltas.
- Long jobs: Background mode (queue → in_progress → completed) with polling/webhooks; not in legacy Completions.

### When to use which
- Use Responses for anything agentic: tools, RAG, structured JSON, multimodal I/O, long/complex tasks, computer use, or when you want typed streaming and better observability.
- Use Chat Completions only for simple, text‑only chat you haven’t migrated yet.
- Use Completions only for strict legacy paths you can’t change yet.

### Capabilities checklist (remember)
- Tools: web search, file search, Code Interpreter, image gen/edit, MCP servers, computer use (where enabled).
- Structured Outputs: enforce JSON Schema; safer integrations; fewer app guardrails.
- Streaming: typed, semantic events (clean partial rendering + progress).
- Background: long‑running tasks with polling/webhooks.
- Reasoning lifecycle: summaries; encrypted items (enterprise).
- Model coverage: GPT‑4o/4.1/o‑series (and successors) expose best capabilities via Responses.

### Migration notes & gotchas
- Shape change: `messages[]` → `input` (plus optional `instructions`). Tools move into `tools: [...]`.
- Structured outputs + tools: To have the model call your function with validated args, set `strict:true` on that tool. If you instead use `response_format.json_schema`, disable parallel tool calls or plan for differing call semantics.
- Parallel tool calls: Default is parallel — your executor must be concurrency‑safe.
- Background: add `"background": true`; handle `queued`/`in_progress`; prefer webhooks for scale.
- Streaming: handle event types, not raw token streams (simplifies front‑ends and logging).
- Assistants API: plan eventual migration; Responses already covers core patterns (tools, files, threads), parity ongoing.
- Security/enterprise: encrypted reasoning items and org controls land in Responses first.

### Quick mental model
- “One call, many capabilities.” Responses is the runtime for agent steps; the Agents SDK (optional) composes many steps. If you only need “chat → text,” Chat Completions is fine; everything else — use Responses.

### Sources (official)
- OpenAI Docs — Migrate to Responses (core agentic primitive; semantic events)
- OpenAI Blog — New tools & features in Responses (MCP, background, reasoning summaries/encrypted items; model coverage)
- OpenAI Docs — Structured Outputs (JSON Schema, `strict:true`)
- OpenAI Docs — Background mode (status lifecycle, polling/webhooks)
- OpenAI Docs — Streaming responses (typed semantic events)
- OpenAI Docs — Using tools (built‑ins + MCP servers), and Web search
- OpenAI Blog — New tools for building agents (positioning; Assistants deprecation target)
- (As of Aug 2025.)

## Solution (revealed after completion)
<div class="solution locked" data-solution-for="01-tokens-and-temp">

=== "Answer notebook"
    Open **[answer.ipynb](answer.ipynb)** (walk-through + outputs).

=== "Answer code (snippet)"
    ```python
    --8<-- "katas/01-tokens-and-temp/solution/solution.py"
    ```

</div>

<div class="admonition tip">
<p class="admonition-title">Done?</p>
<button class="md-button md-button--primary"
        onclick="markKataDone('01-tokens-and-temp');document.querySelectorAll('[data-solution-for=&quot;01-tokens-and-temp&quot;]').forEach(n=>n.classList.remove('locked'));">
  Mark complete
</button>
</div>