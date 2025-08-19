# %% [markdown]
# # 03 · Tools & Function Calling — Question
# **Goal:** Define a tool schema and route a simple intent to it.
# **Time:** 20–25m · **Level:** Intermediate · **Tags:** Tools

# %%
TOOL_SCHEMA = {
    "name": "weather_lookup",
    "description": "Get weather by city name",
    "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"]
    }
}

# %%
def route_and_call(user_input: str) -> str:
    """TODO: classify intent, call tool with args (validated), return final text."""
    # TODO: parse tool call args from model output; mock for now
    return f"Weather in Istanbul is ... (mock)"

# %%
print(route_and_call("What's the weather in Istanbul today?"))