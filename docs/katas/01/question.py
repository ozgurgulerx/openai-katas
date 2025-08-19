# %% [markdown]
# # 01 · Tokens & Temperature — Question
# Explore how `temperature`, `top_p`, and `max_tokens` affect outputs.

# %%
def run_prompt(temp: float, max_new_tokens: int) -> str:
    """TODO: Call your model with the given decoding params and return the text."""
    raise NotImplementedError

# %%
for t in (0.0, 0.4, 0.8):
    print("temp:", t, "| out:", run_prompt(temp=t, max_new_tokens=64))