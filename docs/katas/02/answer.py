# %% [markdown]
# # 02 · Prompt Patterns — Answer (skeleton)
# - JSON mode if available; else strong schema instructions + stops.

# %%
def call_model(prompt: str) -> str:
    # TODO: provider call; return JSON string
    return '{"summary":"ok","facts":["one","two"]}'

# %%
# TODO: show a minimal validator (json.loads + key checks)