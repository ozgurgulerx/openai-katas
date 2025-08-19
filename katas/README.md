# Kata authoring guide

Each kata lives in its own folder, e.g.:

```
katas/01-tokens-and-temp/
├── README.md           # short brief, goals, hints
├── starter/solution.py # starter + reference
├── tests/test_kata.py  # visible tests
├── tests/hidden/       # extra CI-only checks (optional)
└── demo.ipynb          # optional: or use Jupytext-paired .py
```

**Rules of thumb**
- Keep test runs < 2 seconds.
- Prefer Markdown for narrative; use notebooks only when outputs matter.
- If you add notebooks, keep outputs light; avoid huge images in git.