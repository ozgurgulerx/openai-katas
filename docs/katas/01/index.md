---
title: 01 · Tokens & Temperature
---

<script>window.recordKataVisit && window.recordKataVisit('01-tokens-and-temp');</script>

# 01 · Tokens & Temperature
:material-signal: **Goal:** See how `max_tokens`, `temperature`, and `top_p` affect responses.  
**Time:** 10–15m · **Level:** Intro · **Tags:** Prompts, Decoding

## Primer
- `temperature` controls randomness; higher → more diverse outputs.
- `max_tokens` caps generation; small caps truncate.
- `top_p` samples from a probability mass.

## Your task
1. Implement a function that calls the model with variable decoding params.  
2. Compare outputs at `temperature = 0.0, 0.4, 0.8`.  
3. Ensure prompts aren't truncated when `max_tokens` is small.

## Run & verify
```bash
pytest -q
```

??? tip "Hints"
    Keep prompts stable while varying decoding params. Consider seeding if supported.

??? example "Solution (expand)"
    _Solution will be added in the repo's kata folder (`katas/01-tokens-and-temp/`)._

<div class="admonition tip">
<p class="admonition-title">Done?</p>
<button class="md-button md-button--primary" onclick="markKataDone('01-tokens-and-temp')">Mark complete</button>
</div>