# OpenAI Katas

> A clean, hands-on way to learn the OpenAI API platform and modern GenAI builder patterns — by solving small, focused katas that grow in complexity.

## Why this exists
- **Purpose:** Help you get up to speed with OpenAI’s API capabilities quickly and confidently.
- **Approach:** Bite-sized problems/puzzles (katas) arranged from beginner to advanced.
- **Outcome:** Understand core concepts and patterns so you can start building fast.

## What you’ll learn
- **Core API usage:** prompts, messages, streaming, structured outputs.
- **Tool/function calling:** calling functions/tools safely and predictably.
- **Retrieval & RAG:** embeddings, vector stores, retrieval patterns.
- **Agents & orchestration:** multi-step reasoning, planning, and tool use.
- **Multimodal:** text + vision + image generation basics.
- **Production patterns:** evals, observability, rate limits, retries, and safety.

## How it works (the kata format)
Each kata is a small, scoped exercise. Expect:
- **Brief:** what you’re building and why it matters.
- **Objectives:** specific skills or API features to practice.
- **Starter:** minimal scaffolding (or a blank slate) to move fast.
- **Steps:** progressive milestones with hints.
- **Acceptance checks:** simple tests or criteria to validate your solution.
- **Expansions:** optional extra challenges for deeper mastery.

## Tracks & progression
- **Level 0 — Warm-up:** API keys, tokens, costs, and a first request.
- **Level 1 — Essentials:** prompts, system vs user messages, context windows.
- **Level 2 — Tool Calling:** function schemas, JSON outputs, validation.
- **Level 3 — Retrieval:** embeddings, indexing, RAG patterns and pitfalls.
- **Level 4 — Agents:** planning, tool orchestration, multi-turn state.
- **Level 5 — Multimodal:** image understanding/generation, input-output formats.
- **Level 6 — Production:** evals, logging, tracing, retries, fallbacks, safety.

A typical layout will look like this as content lands:
```
openai-katas/
  katas/
    level-0-warmup/
    level-1-essentials/
    level-2-tool-calling/
    level-3-retrieval/
    level-4-agents/
    level-5-multimodal/
    level-6-production/
```

## Getting started
1) **Get an API key** from the OpenAI dashboard and set `OPENAI_API_KEY` in your environment (e.g., `.env`).
2) **Clone** this repository.
3) As katas are published, **open a kata folder** and follow its README.

### Optional sanity check (pick your language)

- JavaScript/TypeScript (Node 18+):

```ts
import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const res = await client.chat.completions.create({
  model: "gpt-4o",
  messages: [
    { role: "system", content: "You are a concise assistant." },
    { role: "user", content: "Reply with 'ready'." }
  ],
  max_tokens: 5
});

console.log(res.choices[0].message.content);
```

- Python (3.10+):

```python
from openai import OpenAI

client = OpenAI()  # Uses OPENAI_API_KEY from env

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are concise."},
        {"role": "user", "content": "Reply with 'ready'."},
    ],
    max_tokens=5,
)

print(resp.choices[0].message.content.strip())
```

## How to use the katas (as they arrive)
- **Pick a kata** that matches your current level.
- **Read the brief** and objectives carefully.
- **Implement iteratively,** running checks at each step.
- **Reflect:** note what generalized pattern you learned.
- **Extend:** try the expansion ideas to deepen understanding.

## Roadmap (high level)
- Level 0–1 initial katas (prompts, context, streaming)
- Tool calling and structured outputs
- Retrieval (embeddings, vector store, RAG)
- Agents and orchestration patterns
- Multimodal basics
- Production hardening (evals, logging, retries, safety)

## Contributing
Contributions are welcome! Feel free to open issues for ideas or PRs for new/updated katas. Keep each kata:
- **Focused** (single concept/pattern)
- **Incremental** (clear progression)
- **Testable** (simple acceptance checks)

---

Made with ❤️ to help you learn faster by building.
