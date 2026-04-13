"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. You might want to:
1. Check if reducing the guest count (e.g., to 250) would work
2. Consider non-vegan venues with vegetarian options
3. Check availability again later (venue status changes)

Would you like me to search with adjusted parameters?
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When I changed The Albanach from `available` to `full` in
`sovereign_agent/tools/mcp_venue_server.py` and re-ran Exercise 4,
Query 1's search results changed from two matches to one match.
The Albanach disappeared and only The Haymarket Vaults remained.

What did not change is the client code, the discovered tool names,
and the final best venue for Query 1. Query 2 also stayed effectively
the same because there were still no venues for 300 guests. This shows
the data/tool layer changed behavior without requiring client updates.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 50   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives a standard tool contract, not just separation into another
file. The client can discover tool names and schemas at runtime, call
them through one protocol, and stay unchanged when server data changes.
That makes the same tool layer reusable across LangGraph and Rasa
without duplicating tool logic in each client.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- A LangGraph research agent should handle open-ended planning because it can decide its own sequence of search, evaluation, and follow-up tool calls when the task is ambiguous.
- A shared MCP server should expose venue search, web research, file operations, and internal business tools so both agents use the same capabilities through one stable interface.
- A Rasa CALM call-handling agent should manage live confirmation conversations because it can enforce deterministic flows, slot collection order, and escalation rules for high-stakes commitments.
- A memory and state layer should store venue shortlists, prior decisions, organiser preferences, and confirmed constraints so both agents work from the same current context.
- A policy and approval layer should enforce limits such as deposit caps, booking cutoffs, and human approval requirements before any external commitment is finalized.
- An observability and cost layer should record traces, tool calls, latency, token usage, and escalation events so the full system can be audited and improved safely.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph agent is the right one for research. In Exercise 2 it
chained several tools on its own, including `check_pub_availability`,
`calculate_catering_cost`, `get_edinburgh_weather`, and
`generate_event_flyer`, and in the out-of-scope train scenario it still
gave a useful fallback answer instead of stopping. In Exercise 4 it
searched venues, then fetched details, and the behavior changed when
the MCP server data changed without rewriting the client.

The CALM agent is the right one for the manager call. In Exercise 3 it
asked for guest count, vegan count, and deposit in a fixed order,
confirmed the booking at £200, escalated at £500, and refused the
parking request with “I’m not trained to help with that.” Swapping them
feels wrong because research benefits from flexible tool-chaining,
whereas confirmation needs narrow, auditable, policy-safe behavior.
"""
