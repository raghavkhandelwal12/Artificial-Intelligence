# Prompt Engineering

**You don't need to be a data scientist or a machine learning Engineer - everyone can write a prompt**

# Introduction to Prompt Engineering(Key Points)

- When thinking about a large language model input and output, a text prompt(sometimes accompanies by other modalities such as image prompts) is the input the model uses to predict a specific output. You don't need to be a data scientist or a machine learning engineer - everyone can write a prompt. However, crafting the most effective prompt can be complicated. Many aspects of your prompt affect its efficacy : The model we use, the model's training data, the model configurations, our-word-choice, style and tone, structure and context all matter. Therefore, prompt engineering is an iterative process.**If our prompt is not clear or detailed enough, the AI give confusing or wrong answer, and it may not be able to give useful result**.


- When we chat with the Gemini Chatbot, we basically write prompts, however this whitepaper focuses on writing prompt for the Gemini model within Vertex AI or by using the API, because by prompting the model directly we will have access to the configuration such as **temprature** etc.

**Explaination of the above paragraph** : 

- The above both paragraph explains the concept of **Prompt engineering for large language model**.

- **Prompt = Input** :  When using LLM, we give it a text prompt(a question or instruction). Sometimes we include other things like images.

- **Output = Prediction** : Based on the prompt, the model predicts and gives an output(like a response, summary, code etc).

- **No Tech Degree Needed** :  We don't need to be a data scientist to write a prompts - anyone can do it.

- **But Good Prompts Take Practice** : Writing a clear and effective prompt is not always easy. We need to think about :

    - The `model` we are using(like GPT-3.5, GPT-4 etc).
    - The `training data` the model was built on.
    - The `setting/configuration used`(e.g. temprature, max tokens).
    - Our `wording, style, tone, and structure`.
    - The `context` we are providing.

# Why it Matters

- A `bad prompt` = bad or vague result.
- A `well-crafted prompt` = accurate, meaning, useful response.
- That's why `prompt engineering is an iterative process` = We often need to try different version of a prompt and improve step by step.


# Prompt Engineering Flowchart

```
START  
  ↓  
Write a Prompt (initial idea)  
  ↓  
Send Prompt to LLM (e.g., ChatGPT)  
  ↓  
Get Output from the Model  
  ↓  
Is Output Accurate/Helpful?  
      ↓Yes                  ↓No  
    [Use it]       →   Modify the Prompt  
                             ↓  
             Add More Context / Clarity  
                             ↓  
            Adjust Tone, Style, Format  
                             ↓  
                Re-send to LLM and Repeat  
```

- When we chat with `Gemini Chatbot`, We are basically writing prompts(just like talking to chatgpt).

- But this `Whitepaper` is not just about chatting. If focuses on using prompts with `Gemini in Vertex AI or via API`.

# Why? Beacuase in those environment, we can:

- `Control Configurations setting(like temprature, max token etc)`.
- These setting affect how the model responds.

# The Whitepaper includes:

- A deep dive into prompt engineering
- Different prompt technique
- Tips and best practices for writing better prompts.
- A section about challenges we might face when writing prompts(like unclear instructions or incomplete context).


# Prompt Engineering With Gemini(Vertex AI/API)

```
START  
  ↓  
Choose Where to Use Gemini  
(Chatbot / Vertex AI / API)  
  ↓  
If Using Vertex AI or API  
→ Access Model Configurations (e.g., temperature, max tokens)  
  ↓  
Write Initial Prompt  
  ↓  
Send Prompt to Gemini  
  ↓  
Get Model Output  
  ↓  
Is the Output Satisfactory?  
      ↓Yes                  ↓No  
    ✅ Use It        🔧 Refine the Prompt  
                             ↓  
               Apply Prompting Techniques  
        (e.g., Few-shot, Zero-shot, Chain-of-Thought)  
                             ↓  
              Use Tips & Best Practices  
                             ↓  
                Re-send and Evaluate Again  
                             ↓  
                  Note Challenges Faced  
                             ↓  
          Learn & Improve Prompting Skills  

```
