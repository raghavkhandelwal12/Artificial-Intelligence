# ReAct

- `Reason and act(ReAct)` prompting is a paradigm for enabling LLMs to solve complex tasks using `natural language reasoning` combined with external tools `(search, code, interpreter etc.)` allowing to LLMs to `perform certain actions`, `such as interacting with external APIs to retrieve information which is first step towards agent modeling.`

- `ReAct` mimics how human operate in real world, as we reason verbally can  take actions to gain information. `ReAct` perform well `against other prompt engineering aproaches in a variety of domains.`

- `ReAct Prompting` works by `combining reasoning and acting into a thought-action loop`. The LLM first reasons about the problem and generates a plan of actions. It them performs the actions in the plan and observe the result. The `LLM uses the observations to update its reasoning and generate a new plan of action`. This process continues until the LLM reaches a solution to the problem.
# ReAct

- `ReAct` Prompting stand for `Reasoning and Acting`. It is a powerful technique that combine `logical Thinking(reasoning) with actionable operations(calling tools, APIs, Calculators, Databases)`. This method allows LLMs to reason step-by-step and take real-time actions to improve decision-making and accuracy in multi-step tasks.

# Architecture Structure

**Architecture Breakdown** : 

1. `Thought` : The model reasons about what to do.
2. `Action` : Based on reasoning, it calls a tool(e.g, search, calculator).
3. `Observation` : The result of that action is received.
4. `Though` : It processes the observation and continues.
5. `Final Answer` : After multiple thought Action observation loops. It concludes with an answer.

# Tokenization & Context Memory

`Tokenization & Positional Embedding`
- Each step(Thought, Action, Observation) is converted to tokens.
- Positional Encoding helps maintain multi-step sequence integrity.
- Context length must be large enough to store all history


# Transformer  Reasoning Flow

`Reasoning + Tool-Action Planning` : 
- Transformers attention allows the model to track tool results.
- Thought steps are logically dependent or prior Observations.
- Model develops a chain of control similar to a function pipeline.

# Sampling & Execution Setting

`Sampling & Generation Settings`:
- Temprature : 0.3 to 0.5 for stable step-by-step  generation.
- Top-K : 40 | Top-P:0.9
- Token limit must be support extended multi-turn dialogue.
- Output continues until answer or max context is hit.

# Prompt Example

`Question : What is the square root of the year Einstein was born?`

`Thought : Let's first find Einstein's birth year.`
`Action : Search["Einstein birth year"]`
`Observation : 1879`
`Thought : Now calculate sqrt(1879)`
`Action : Calculator[sqrt(1879)]`
`Observation : 43.35`
`Answer : 43.35`.

# Python code example
```
 prompt = '''
 Question: What is the square root of the year Einstein was born?
 Thought: Let's first find Einstein's birth year.
 Action: Search["Einstein birth year"]
 Observation: 1879
 Thought: Now calculate sqrt(1879)
 Action: Calculator[sqrt(1879)]
 Observation: 43.35
 Answer: 
 ```
 ```
 from transformers import pipeline
 generator = pipeline("text-generation", model="gpt2")
 result = generator(prompt, max_length=150, temperature=0.4)
 print(result[0]["generated_text"])
 ```

 # Conclusion
 - ReAct prompting is ideal for tasks requiring dynamic data, tool interaction, and real-time logic. It supports high-quality decision chains and enables models to behave like autonomous agent. This technique is foundational for advanced AI assistants, agents and chatbots that perform live operations.


# What is Reason and Act(ReAct) Prompting

- `ReAct Prompting` is a method used in prompting large language model like ChatGpt `where the model does not think or generate text, but also acts. This approach mimics how humans solve real-world Problems - We think, act to gather information, then revise our thinking based on new information`.

**Natural Language Reasoning** : This means the LLM uses `plain human-like language` to :
- `Think through a problem`.
- `Make Logical Deductions`.
- `Decide on a plan of actions`.
```
It mimics human thinking: think → act → observe → update thinking → act again... until the answer is found.
```

# ReAct in Action(Example Summary)

**You are asking an LLM** : `"How many kids do the band members of Metallica have?"`

**ReAct Loop Flow** : 

1. `LLM Think` : "Let's Find out how many band members Metallica has".
2. `Action(Search)` : "How many kids does James Hetifield have?".
3. `Observation` : "James has 3 kids".
4. `Reason Update` : "Okay, 1/4 members = 3 kids so far"
5. Repeat for each memeber.
6. `Final Answer` : 10 kids from 4 member.

```
#  ReAct in Action: Metallica Kids Example

##  Task
**Prompt to the LLM:**  
"How many kids do the band members of Metallica have?"

The ReAct (Reason + Act) paradigm allows the AI to:
- **Reason** about what needs to be done,
- **Act** using tools like search APIs,
- **Observe** the results,
- **Update** its thinking and repeat the process.

---

##  ReAct Loop Explained

### Step 1: Understand the Question
The AI sees the question and starts with a plan:
> "I need to find out how many kids each member of Metallica has."

---

### Step 2: Initial Thought
> "Let me find out who the band members are."

###  Action (Search):
**Query:** "Who are the members of Metallica?"

###  Observation:
> Metallica has 4 members:
- James Hetfield
- Lars Ulrich
- Kirk Hammett
- Robert Trujillo

---

## Looping Through Each Member

###  James Hetfield
- **Thought:** Let’s find out how many kids James has.
- **Action:** Search "How many kids does James Hetfield have?"
- **Observation:** James has **3 children**.
- **Reason Update:** 1/4 members → 3 kids total so far.

---

### Lars Ulrich
- **Action:** Search "How many kids does Lars Ulrich have?"
- **Observation:** Lars has **3 children**.
- **Reason Update:** 2/4 members → 3 + 3 = **6 kids**.

---

###  Kirk Hammett
- **Action:** Search "How many kids does Kirk Hammett have?"
- **Observation:** Kirk has **2 children**.
- **Reason Update:** 3/4 members → 6 + 2 = **8 kids**.

---

###  Robert Trujillo
- **Action:** Search "How many kids does Robert Trujillo have?"
- **Observation:** Robert has **2 children**.
- **Reason Update:** 4/4 members → 8 + 2 = **10 kids**.

---

## Final Answer
> The total number of kids Metallica band members have is **10**.

---

## ReAct Loop Flowchart Summary

```plaintext
1. Think → Who are the band members?
2. Act (Search) → Get band member names
3. Think → Find number of kids per member
4. Act (Search) → Query each member
5. Observe → Get number of kids
6. Update → Keep adding total
7. Repeat until all members are done
8. Final Answer → Total kids = 10

```


# The Full ReAct Loop

```
1. Think → What's the goal?
2. Act → Use a tool to find information.
3. Observe → Read the result.
4. Update → Add new info to memory.
5. Repeat → Until the task is complete.
```

# Detailed Explanation of Every Concept and Word.

- `LLM` : Large Language Modle(Like ChatGPT or VertexAI).
- `Reason` : Logical Thinking using Language.
- `Act` : Doing something Outside the model(e.g web search).
- `Langchain` : A python framework to build LLM-based applications.
- `VertexAI` : Google Cloud service for AI models.
- `SerpAI` : API to search google and return result.
- `Agent` :  A system that combines LLM + tools  and perform reasoning/actions.
- `Zero_Shot_React_Description` : A special langchain agent type that follow ReAct logic.
- `Thought-Action Loop` : Repeating pattern of thing-act-observe-re-think.

```
 ┌───────────────┐
 │  User Prompt  │
 └─────┬─────────┘
       ↓
 ┌───────────────┐
 │    LLM Think  │──→ e.g., "Let's check band members"
 └─────┬─────────┘
       ↓
 ┌───────────────┐
 │   Action      │──→ Use SerpAPI to search web
 └─────┬─────────┘
       ↓
 ┌───────────────┐
 │ Observation   │──→ e.g., "James Hetfield has 3 kids"
 └─────┬─────────┘
       ↓
 ┌───────────────┐
 │ Update Reason │──→ Continue thought based on new info
 └─────┬─────────┘
       ↓
      Loop
       ↓
 ┌───────────────┐
 │ Final Answer  │──→ e.g., "10 kids"
 └───────────────┘
```

- `ReAct Prompting` in practice require understanding that we continually have to resend the previous prompts/responses(and do trimming of the extra generated content) as well as set up the model with appropriate example/instructions.




