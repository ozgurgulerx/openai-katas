# %% [markdown]
# # 01 · Tokens & Temperature — Answer
# Reference implementation + quick comparison loop.

# %%
def run_prompt(temp: float, max_new_tokens: int) -> str:
    # Pseudo-code: replace with your SDK call
    return f"(temp={temp}, max_new={max_new_tokens}) demo"

# %%
for t in (0.0, 0.4, 0.8):
    print("temp:", t, "| out:", run_prompt(temp=t, max_new_tokens=64))