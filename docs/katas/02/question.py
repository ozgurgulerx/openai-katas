# %% [markdown]
# # 02 · Prompt Patterns — Question
# **Goal:** Produce robust JSON via prompt design (or JSON mode).
# **Time:** 15–20m · **Level:** Intro · **Tags:** Prompts, Structure

# %% [markdown]
# ## 1) Pattern objective
# - Enforce structure (JSON schema / keys).
# - Guard against instruction bleed via clear delimiters.

# %%
EXAMPLE_INPUT = {"name": "Ada Lovelace", "year": 1843}
# TODO: write a prompt that yields strictly valid JSON with keys: summary, facts[]

# %%
def call_model(prompt: str) -> str:
    """TODO: replace with provider call returning raw text."""
    return '{"summary":"TODO","facts":["TODO"]}'

# %%
raw = call_model("PROMPT_GOES_HERE")
print(raw)

# %% [markdown]
# ## 2) Validation
# - Parse as JSON.
# - Check required keys; report errors if missing.