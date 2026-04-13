"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                 
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                   
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                          
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                 
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                              
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                       
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                              
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking                              
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                 
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
For out-of-scope requests, CALM politely declines and redirects the user
to the appropriate contact. It also offers to continue with the original
booking confirmation flow, ensuring a smooth user experience while
maintaining boundaries.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM handled the parking question much more rigidly than the
LangGraph agent. CALM recognized that the request was outside the
booking-confirmation flow, refused it, and steered the conversation back
to the original task. In Exercise 2 Scenario 3, the LangGraph agent was
more flexible: it explained that train times were outside its scope,
suggested external sources like National Rail and Trainline, and then
offered help with related planning tasks. So CALM was narrower and more
controlled, while LangGraph was more conversational and improvisational.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by temporarily changing the condition to
`if True` in `exercise3_rasa/actions/actions.py`, then retraining and
restarting the Rasa action server and chat. I ran a normal
booking-confirmation conversation and verified that the agent escalated
immediately with the time-based cutoff reason. After that, I reverted
the test change back to the real `datetime.datetime.now()` condition.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM is simpler because the LLM now handles intent recognition and slot
extraction from natural speech, so we no longer need `nlu.yml`,
`rules.yml`, or regex-heavy validation code. Python still keeps the
important part: deterministic business rules in `ActionValidateBooking`.
The tradeoff is that CALM is easier to build and more natural for users,
but slightly less transparent than the old rule-and-regex approach at
the language-understanding layer.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM still costs more setup than LangGraph: config files, training, an
action server, endpoints, and a Rasa Pro licence. What you get back is
control. The assistant can only follow the flows and actions we defined,
which makes behaviour easier to read, test, and audit. It cannot
improvise new tasks or call undefined tools like LangGraph could. For
booking confirmation, that limitation is mostly a feature.
"""
