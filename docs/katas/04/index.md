---
title: 04 · Evals & Caching
---
<script>window.recordKataVisit && window.recordKataVisit('04-evals-caching');</script>
# 04 · Evals & Caching
**Time:** 20–25m · **Level:** Intermediate · **Tags:** Evals, Caching
## Primer
- Regression tests for prompts; cache hot paths to cut cost/latency.
## Your task
Create two eval cases and cache a deterministic subroutine.
## Run & verify
```bash
pytest -q
```
??? tip "Hints"
    Separate stochastic steps from cached deterministic calls.
??? example "Solution (expand)"
    _See repo kata folder._
<div class="admonition tip"><p class="admonition-title">Done?</p>
<button class="md-button md-button--primary" onclick="markKataDone('04-evals-caching')">Mark complete</button>
</div>