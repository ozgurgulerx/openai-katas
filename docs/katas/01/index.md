---
title: 01 · Tokens & Temperature
---
<script>window.recordKataVisit && window.recordKataVisit('01-tokens-and-temp');</script>

# 01 · Tokens & Temperature
**Time:** 10–15m · **Level:** Intro · **Tags:** Prompts, Decoding  
[:octicons-codespaces-16: Open Codespace in this kata](https://github.com/codespaces/new/ozgurgulerx/openai-katas?quickstart=1#folder=/katas/01-tokens-and-temp)

=== "Markdown question"
    ## Primer
    - `temperature` controls randomness; higher → more diverse outputs.
    - `max_tokens` caps generation; small caps truncate.
    - `top_p` samples from probability mass.

    ## Your task
    1. Implement `run_prompt(temp, max_new_tokens)`.
    2. Compare outputs at `0.0, 0.4, 0.8`.
    3. Avoid truncation with small caps.

    ## Run & verify
    ```bash
    pytest -q
    ```

=== "Notebook question"
    Open the notebook version: **[question.ipynb](question.ipynb)**

--- 

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