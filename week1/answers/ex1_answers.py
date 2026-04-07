"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults" 
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions correct. This is common on strong models with clean data. PLAIN used 180 tokens, XML - 251 tokens, SANDWICH - 289 tokens.
Notice that the XML and SANDWICH answers are the same, but different from PLAIN - formatting changes can change the answer.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Haymarket Vaults"
PART_B_SANDWICH_ANSWER = "The Haymarket Vaults"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Distractors didn't cause any wrong answers. The Holyrood Arms is the most dangerous: it satisfies capacity AND vegan,
only failing on status. A model that skims rather than evaluating all three constraints will likely pick this one.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults" 
PART_C_XML_ANSWER      = "The Haymarket Vaults" 
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults" 

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Again all the results are correct. The small model is more sensitive to context formatting, though in this case worked.
The answers for XML and SANDWICH now changed to "The Haymarket Vaults" - which is still correct.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Presentation conditions (plain / XML / sandwich) can chnage the answer, but in this case all three formats worked. 
The small model is more sensitive to formatting, but again all three formats worked.
Distractors can cause wrong answers if the model skims rather than evaluating all constraints, but in this case all three formats worked.
"""
