# %% [markdown]
# # 04 · Evals & Caching — Question
# **Goal:** Add two regression evals and cache a deterministic substep.
# **Time:** 20–25m · **Level:** Intermediate · **Tags:** Evals, Caching

# %%
def normalize(text: str) -> str:
    """Deterministic step (safe to cache)."""
    return " ".join(text.lower().split())

# %%
# TODO: add a tiny cache dict around normalize() or your retrieval step
CACHE = {}

# %%
TESTS = [
    {"inp": "Hello  WORLD", "expect_contains": "hello world"},
    {"inp": "Foo\tBar", "expect_contains": "foo bar"},
]

# %%
def run_eval():
    ok = True
    for t in TESTS:
        out = normalize(t["inp"])
        if t["expect_contains"] not in out:
            ok = False
            print("FAIL:", t, "→", out)
    print("EVAL:", "PASS" if ok else "FAIL")

# %%
run_eval()