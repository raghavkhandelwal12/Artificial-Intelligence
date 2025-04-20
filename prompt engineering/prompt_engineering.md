# Prompt Engineering
- Remember how an LLM works; It's a prediction engine. The model takes sequential text as input and then predicts what the following token should be, based on the data it was trained on. The LLM is operationalized to do this over and over again, adding the previously predicted token to the end of the sequential text for predicting the following token. The next token prediction is based on the relationship between what's in the previous tokens and what the LLM has been seen during its training.

- When we write a prompt, you are attempting to set up the LLM to predict the right sequence of tokens. Prompt engineering is the process of designing high-quality prompts that guide LLMs to produce accurate outputs. This process involves tinkering to find the best prompt, optimizing prompt length, and evaluating a prompt's writing style and structure in relation to the task. In the context of natural language processing and LLMs, a prompt is an input provided to the model to generate a response or prediction.

- These prompts can be used to achieve various kinds of understanding and generation tasks such as `summarization, information extraction, question and answering, text classification, language or code translation, code generation, and code documentation or reasoning`.

- When prompt engineering, we start by choosing a model. Prompts might need to be optimized for our specific model, regardless of whether  we sue Gemini language models in Vertex AI, GPT, Claude, or an open source model like Gemma or LLama.

  # Explain Of How an LLM works as a Prediction Engine

A `Large Language model` is essentially a prediction engine. It predict the next word, character or token in a sequence based on the input text provided. Here's step by step breakdown of how it work.

1. `Input Sequential Text` : The model receives a sequence of words or tokens as input. This sequence can be sentence, phrase or even a single word.

2. `Contextual Analysis` : The model process the input sequence and understand the relationship between the tokens. This involves understanding the context based on the previous tokens. For example, if the input is `I am going to the`, the model consider the context to predict the next word or might be `store or park`.

3. `Prediction of Next Tokens` : Based on the context and the data model has been trained on, it predicts the next token(e.g. the next word or character). This prediction is influenced by the statistic relationship the model has learned between tokens during training.

4. `Add predicted Tokens to Sequence` : After predicting the next tokens, the model appends it to the existing sequence, effectively growing the sequence by one token.

5. `Repeat the Process` : This new sequence is then used as the input for the next token prediction. The model continuously repeat this process, generating tokens one after the other, until it reaches the end of the sequence for meets a stopping condition(e.g. maximum length, special end-of-sequence token).

6. `Output` :  Finally after the model has predicted all the tokens it outputs the complete sequence of text.


```
       +--------------------------+
        |    Input Sequential Text |
        +--------------------------+
                     |
                     v
        +---------------------------+
        | Analyze Previous Tokens   |
        | (Context from Input)       |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Predict Next Token         |
        | (Based on Training Data)   |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Add Predicted Token to     |
        | the Input Sequence         |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Repeat Process for Next    |
        | Token Prediction           |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Output Final Sequence      |
        +---------------------------+
```


# Prompt Engineering

- When we write a prompt, we are attempting to set up the LLM to predict the right sequence of tokens.

- `Prompt Engineering` is the process to designing the `high-quality of prompts` that guide to LLM to `produce the accurate output`. This process involves the `tinkering to find the best prompts, optimizing prompt lenght, and evaluating a promt's writing style and structure to the task`. In the context of natural language processing and LLMs, a prompt is an input provided to the model to generate a response or prediction.

- These prompt can be used to achieve to understanding and generation tasks such as `text summarization, information extraction, question and answering, text classification, language or code translation, code generation, and code documentation or reasoning`.

- When prompt engineering, we start by choosing a model. Prompt might need to be optimized for our specific model, regardless of whether to use Gemini language model in Vertex AI, GPT, Claude, or an open source model like Gemma or LLAMA.

### 🔁 Prompt Engineering Flow for LLMs

```
START  
  ↓  
Choose an LLM (e.g., Gemini, GPT, Claude)  
  ↓  
Define Your Task  
(Summarization, Q&A, Code Gen, etc.)  
  ↓  
Write an Initial Prompt  
  ↓  
Set Model Configurations  
(temperature, max tokens, top-k, etc.)  
  ↓  
Send Prompt to LLM  
  ↓  
Receive Output  
  ↓  
Is the Output Useful?  
      ↓Yes                  ↓No  
    ✅ Use It        🔁 Refine Prompt or Tune Configs  
                             ↓  
                Adjust Style, Length, Context  
                             ↓  
                Re-send Prompt and Iterate  
```
