# Automatic Prompt Engineering
- `Automatic Prompt Engineering(APE)` is an approach that automates `the process of generating prompts, evaluating them, and refining them to enhance the performance of AI models`. This method is useful in variety of tasks, especially `when it is important to generate multiple variation of prompts to ensure that AI system can handle diverse ways of expressing similar ideas.`

# Steps of Automatic Prompt Engineering(APE)

1. `Initial Prompt Creation` : The first step is to create an `initial prompt that will instruct the model to generate differt variants of a prompt`. The `initial prompt specifies the task and the goal`, such as asking the model to generate alternative ways of phrasing an order for a product in a webshop.

- `Example` : Suppose you are training a chatbot for a t-shirt webshop. You want the chatbot to understand various wasy a customer might request a t-shirt order.

    - `Initial Prompt` : "We have a band merchandise t-shirt webshop, and to train a chatbot we need various ways to order: One Metallica t-shirt size S'. Generate 10 variants, with the same semantics but keeping the same meaning.

2. `Generation of Output Variants` : Using an LLM(Large Language Modle) `like Gemini-Pro or GPT`, we generate multiple variants of the same prompt. The goal is to produce multiple ways to phrase the same instruction while keeping the original meaning intact.

**Example Output Variants(Generate for the prompt)**

1. I'd like to purchase a Metallica t-shirt in size small.
2. Can I order a small-sized Metallica t-shirt?.
3. I'd like to buy one Metallica t-shirt in small.
4. One Metallica shirt, size small, please.
5. I want one Metallica t-shirt in size small.
6. I'd like to place an order for one Metallica t-shirt in small.
7. Small Metallica t-shirt, one please.
8. I'm looking for one Metallica t-shirt in small.
9. Can you get me one Metallica t-shirt in small.
10. One Metallica small t-shirt, please.

3. `Evaluate the Generate Variants` : Once the model generates multiple variants, the next step is to evaluate these variants based on a specific metric. Common Evalation metric include.

- `BLEU(Bilingual Evaluation Understudy)` : Measures the overlap between the generated text and a reference text. BLEU is often used for `translation tasks and can help determine how well the generated prompts preserve the original meaning`.

**Example** 

- `Reference Sentence` : "The cat is sitting on the mat"
- `Generated Sentence` : "The cat sits on the mat".

**How BLEU Works** : 

- `BLEU` will check how many words in the `generated sentence`("The", "cat", "on", "the", "mat") match the `reference sentence`("The", "cat", "is", "sitting", "on", "the", "mat")
- It gives a score based on `Word overlap`. Even though "sitting" is replace with "sits" . BLEU still gives a relatively good score since most words. It is about `Precision`.

- `ROUGE(Recall-Oriented Understudy for Gisting Evaluation)` : Focuses on the recall of n-grams between the `generated text and referece texts`. It's commonly used for summarization tasks.

**Example** : 

- `Reference Text` : "The cat is sitting on the mat, and it looks comfortable".
- `Generated Text` : "The cat is sitting on the mat".

**How ROUGE Works** : 
- `ROUGE` focuses on the `recall`- how much of the information form the reference is in the generated text.
- Here, ROUGE will look for the key information:` "cat," "sitting," and "mat."` The generated text includes most of the important content, so ROUGE would give a good score, though it might lose points for missing the part about the cat "looking comfortable."

- `Evaluation Process` : Each variant generated in the previous step is evaluated for how well it aligns with the original task, the fluency of the sentence, and its clarity. The candidate prompts are assigned a score based on the metric used.

4. `Selection of the Best Candidate` : After evaluating all the variants, we select the prompt that scores the highest. This selected prompt is them used in the chatbot or software application.

- `Tweaking` : Sometime, we may need to manually tweak the selected prompt(for example, rephrasing a word or correcting a small grammatical error) to solve optimize it for the intended use.

5. `Iterate` : The final step in `APE` is to repeat the process. After tweaking the selected prompt, we might want to evaluate again and generate new variant. The process of refining and selecting prompts continue until the optimal prompt is found.

# Flowchart

```
+--------------------------------------+
|     Step 1: Initial Prompt Creation |
+--------------------------------------+
               ↓
+----------------------------------------+
| Step 2: Generate Multiple Variants     |
| (Model generates different variants)   |
+----------------------------------------+
               ↓
+----------------------------------------+
| Step 3: Evaluate Variants              |
| (Use BLEU, ROUGE, etc., to score)      |
+----------------------------------------+
               ↓
+----------------------------------------+
| Step 4: Select Best Variant           |
| (Choose prompt with highest score)    |
+----------------------------------------+
               ↓
+----------------------------------------+
| Step 5: Tweak & Refine Selected Prompt |
| (Optional manual editing)              |
+----------------------------------------+
               ↓
+----------------------------------------+
| Step 6: Re-evaluate (if needed)        |
| (Re-check with a new evaluation score) |
+----------------------------------------+
               ↓
+----------------------------------------+
| Step 7: Finalized Prompt for Use      |
| (Implement in chatbot or application) |
+----------------------------------------+

```


