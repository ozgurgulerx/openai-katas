# %% [markdown]
# # 05 · Agents 101 — Question
# **Goal:** Minimal plan→(maybe)act→observe loop with a single tool.
# **Time:** 25–30m · **Level:** Intermediate · **Tags:** Agents

# %%
MAX_STEPS = 3

def tool_echo(text: str) -> str:
    return f"[tool] {text}"

def agent(query: str) -> str:
    """TODO: decide: answer directly or call tool_echo once; stop within MAX_STEPS."""
    steps = 0
    reply = "(TODO)"
    # TODO: simple heuristic or model call to choose action
    return reply

# %%
print(agent("Echo 'hello' once, then stop."))