# %% [markdown]
# # 01 · Responses API — Simple Text Generation — Question
# **Goal:** Make a single call to the OpenAI Responses API that returns text.
# **Time:** 10–15m · **Level:** Intro · **Tags:** API, Responses, Text
# ---
# ### What you'll build
# - A tiny function that calls the Responses API with a prompt and returns text.
# - A one-off demo invocation printing the generated text.
#
# ### Prereqs
# - `OPENAI_API_KEY` available as env var.
# - OpenAI Python SDK installed (or wire up your provider SDK similarly).

# %% [markdown]
# ## 1) Imports & setup (TODO: choose your SDK)
# Replace with the SDK you use. For OpenAI Python:
#   from openai import OpenAI
#   client = OpenAI()

# %%
import os
from typing import Any
# TODO: from openai import OpenAI
# TODO: client = OpenAI()  # or your provider client

# %% [markdown]
# ## 2) Implement the core function
# - Accept a plain text `prompt` and (optionally) a `model` name.
# - Call the Responses API and return the output text as `str`.

# %%
def run_prompt(prompt: str, model: str = "gpt-4o-mini") -> str:
    """TODO: Call the OpenAI Responses API with the given prompt and return text.

    Example (OpenAI Python SDK):
        # resp = client.responses.create(
        #     model=model,
        #     input=prompt,
        # )
        # return resp.output_text  # Convenience property (SDK >= 1.x)
    """
    # TODO: replace with an actual Responses API call; below is placeholder
    return f"[demo] model={model} prompt_len={len(prompt)}"

# %% [markdown]
# ## 3) Demo
# Make a single call and print the generated text.

# %%
if __name__ == "__main__":
    prompt = "Write one cheerful sentence about learning the Responses API."
    out = run_prompt(prompt)
    print(out)

# %% [markdown]
# ## 4) Notes
# - Responses API is the unified, tool-native endpoint; use it for text and more.
# - Start simple (text-only); later add tools, structured outputs, or background mode.
# - Prefer Responses over legacy Completions/Chat Completions for new work.