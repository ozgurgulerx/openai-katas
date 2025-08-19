# %% [markdown]
# # 01 · Responses API — Simple Text Generation — Answer (skeleton)
# Reference scaffold; replace placeholders with your actual SDK calls.
#
# ### Approach
# - Accept a plain text prompt.
# - Call the OpenAI Responses API once and return the text output.

# %%
from typing import Any

def run_prompt(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Reference: simple text generation via Responses API.

    Example (OpenAI Python SDK):
        # from openai import OpenAI
        # client = OpenAI()
        # resp = client.responses.create(model=model, input=prompt)
        # return resp.output_text
    """
    # TODO: wire to your SDK; keep signature stable for any checks
    return f"(ref) model={model} prompt_len={len(prompt)}"

# %%
if __name__ == "__main__":
    print("ref:", run_prompt("Write one cheerful sentence about learning the Responses API."))