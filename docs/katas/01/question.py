# %% [markdown]
# # 01 · Tokens & Temperature — Question
# **Goal:** Observe how `temperature`, `top_p`, and `max_tokens` affect responses.
# **Time:** 10–15m · **Level:** Intro · **Tags:** Prompts, Decoding
# ---
# ### What you'll build
# - A tiny function that calls your model with given decoding params.
# - A short loop to compare outputs at different temperatures.
#
# ### Prereqs
# - `OPENAI_API_KEY` (or your provider's key) available as env var.
# - SDK installed in the devcontainer.

# %% [markdown]
# ## 1) Imports & setup (TODO: choose your SDK)
# Replace with the SDK you use (OpenAI, Azure OpenAI, Anthropic, etc.)

# %%
import os
from typing import Any
# TODO: from openai import OpenAI
# TODO: client = OpenAI()  # or your provider client

# %% [markdown]
# ## 2) Implement the core function
# - Keep the prompt stable; vary only decoding params.
# - Return `str` for easy comparison.

# %%
def run_prompt(temp: float, max_new_tokens: int, top_p: float = 1.0) -> str:
    """TODO: call model with given decoding params and return the text."""
    # TODO: replace with an actual call; below is placeholder
    return f"[demo] temp={temp} max_new={max_new_tokens} top_p={top_p}"

# %% [markdown]
# ## 3) Experiments
# Try temperature in (0.0, 0.4, 0.8); watch output diversity and truncation behavior.

# %%
for t in (0.0, 0.4, 0.8):
    out = run_prompt(temp=t, max_new_tokens=64, top_p=0.95)
    print(f"temp={t} → {out}")

# %% [markdown]
# ## 4) Notes
# - Low temperature ≈ deterministic, good for evals.
# - High temperature ≈ ideation, but less stable.
# - `max_tokens` too small → truncation risk.