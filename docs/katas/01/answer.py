# %% [markdown]
# # 01 · Tokens & Temperature — Answer (skeleton)
# Reference scaffold; replace placeholders with your actual SDK calls.
#
# ### Approach
# - Stable system/user prompt.
# - Vary decoding params only.

# %%
from typing import Any

def run_prompt(temp: float, max_new_tokens: int, top_p: float = 1.0) -> str:
    # TODO: wire to your SDK; keep signature stable for tests
    return f"(ref) temp={temp} max_new={max_new_tokens} top_p={top_p}"

# %%
for t in (0.0, 0.4, 0.8):
    print("ref:", run_prompt(temp=t, max_new_tokens=64, top_p=0.95))