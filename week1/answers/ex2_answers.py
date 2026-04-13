"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = '''
Was getting 'No tool calls were made' error until I switched to the Qwen3-32B model and did some code changes in 
research_agent.py to properly fix the trace extraction"
'''

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-1d747081-f80b-44fe-8504-a1cb8f864487_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The user wanted to check The Bow Bar for 160 vegan guests. The response from the tool says that The Bow Bar has a capacity of 80, which is less than the required 160. So it doesn't meet the capacity constraint
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = None   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known Edinburgh venues can accommodate 300 people with vegan options. The maximum capacity among the checked venues is 200 (The Guilford Arms), but it lacks vegan options. The Bow Bar has vegan options but is currently full and only seats 80.\n\nWould you like me to:\n1. Suggest alternative venues outside our known list?\n2. Help adjust requirements (e.g., reduce guest count or dietary restrictions)?\n3. Check availability for a different date?"
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """
I don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:\n1. The National Rail website (https://www.nationalrail.co.uk)\n2. Train service apps like Citymapper or Trainline\n3. The specific train operator's website (e.g., LNER)\n\nWould you like help with anything related to Edinburgh pubs, weather, or event planning instead?
"""


# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Handled all three scenarios in a way that seems reasonable for a booking assistant. In scenario 1, it correctly identified the capacity issue and pivoted to an alternative venue. In scenario 2, it acknowledged the impossible constraint and offered helpful next steps without hallucinating. In scenario 3, it recognized the out-of-scope request and provided a polite response with useful suggestions.
Although in scenario 3 it could have just refused to answer and asked the user about booking instead.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph Mermaid output is very abstract: it only shows a single loop where the agent decides whether to end or call tools, then reasons again after each tool result. 
By contrast, `exercise3_rasa/data/flows.yml` is explicit and task-specific. It defines concrete flows like `confirm_booking` and `handle_out_of_scope`, fixes the slot collection order, and ends with a named validation action. 
LangGraph is more flexible but less predictable, while CALM is more constrained, readable, and auditable.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
Nothing really unexpected. Thought it mught hallucinate more in scenario 2 but it handled it well. In scenario 3, I was half expecting it to try to call a tool or give a made-up train time, but instead it gave a reasonable refusal and suggestions for next steps.
"""
