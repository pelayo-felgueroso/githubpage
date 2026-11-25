---
title: "Large Language Models" 
---
A **Large Language Model (LLM)** is an [[AI model]] trained on large amounts of text to understand and generate human language.

LLMs learn patterns and relationships between words, concepts and ideas. This allows them to answer questions, explain topics, summarise information, write code and much more.

They are based on neural networks, particularly an architecture called the [[Transformer]]. They generate text by predicting what comes next, one piece at a time, based on the context they receive.

LLMs can also be used as the core of [[Agents]], which can use tools, perform actions and work towards specific goals instead of only generating text.

Examples include ChatGPT, Claude and Gemini.

## Explanation

### Architecture

Most LLMs today are built on the [[Transformer]] architecture, a deep learning architecture based on the **attention** mechanism. It was introduced in 2017 and gained wide interest after Google released BERT in 2018.

LLMs come in various forms, but they are typically decoder-based models with **billions of parameters**. Some well-known LLMs:

|**Model**|**Provider**|
|---|---|
|**Deepseek-R1**|DeepSeek|
|**GPT-4**|OpenAI|
|**Llama 3**|Meta (Facebook AI Research)|
|**SmolLM2**|Hugging Face|
|**Gemma**|Google|
|**Mistral**|Mistral|

### Tokens

The core principle of an LLM is simple: **it predicts the next token, given a sequence of previous tokens**.

A **token** is the unit of information an LLM works with. You can think of a token as a word, but for efficiency LLMs work with sub-word units that can be combined. For example, while English has an estimated 600,000 words, an LLM might have a vocabulary of around 32,000 tokens (as is the case with Llama 2).

You can experiment with different tokenizers in the interactive playground below:

<iframe src="https://agents-course-the-tokenizer-playground.static.hf.space/" width="100%" height="600" style="border: none; border-radius: 8px;" loading="lazy" title="Tokenizer Playground" ></iframe>

Each LLM also has **special tokens** that mark the structure of its input and output, for example the start or end of a sequence, a message or a response. The most important one is the **End of Sequence token (EOS)**, which tells the model to stop generating.

### Next-token prediction

LLMs are **autoregressive**: **the output of one step becomes the input of the next**. The model keeps generating tokens in a loop until it predicts the EOS token.

In each step of the loop:

1. The input text is **tokenized**.
2. The model computes a representation of the sequence that captures the meaning and position of each token.
3. From that representation, the model outputs a score for every token in its vocabulary, ranking how likely each one is to come next.

### Decoding strategies

Once every token has a score, a decoding strategy chooses which one to use:

- **Greedy:** always take the token with the highest score.
- **Beam search:** keep several possible continuations at once and, at the end, choose the one with the best overall score. A token that wasn't the top choice at one step can lead to a better sentence overall.

### Attention

When predicting the next token, not every earlier token is equally relevant. In "The capital of France is...", the words **capital** and **France** decide the answer, while "the" and "of" barely matter. **Attention** is the part of the model that determines how much each earlier token should influence the prediction.

### Context length

The **context length** is the maximum number of tokens the model can take into account at once: the input plus everything generated so far. Anything beyond that limit isn't seen. In Ollama, for example, it's set with `num_ctx` (e.g. `num_ctx=4096`).

### The prompt

The **prompt** is the text you give the model. Because the output depends entirely on that text, how you write it matters: clear, specific instructions produce better results.

### Training

- **Pre-training:** the model is trained on huge amounts of text with one task, predicting the next token. No manual labelling is needed, because the correct answer is always the next token in the text. This is how it learns language, facts and patterns.
- **Fine-tuning:** afterwards, it receives further training for specific behaviours, such as holding a conversation, using tools or writing code.

### Ways to use an LLM

- **Locally**, on your own computer, for example with Ollama.
- **Through an API in the cloud**, using a provider's servers.

## Resources

_Learn more from external sources._

- [Computerphile – Why AI Tokens are so Expensive](https://www.youtube.com/watch?v=-0HRzXk8vlk)
    
- [Computerphile – AI Language  Models & Transformers](https://www.youtube.com/watch?v=rURRYI66E54)
    
- [Ilia – LLMs Meet Robotics: What Are Vision-Language-Action Models?](https://www.youtube.com/watch?v=8dZUOo5xWFw) 

## Related concepts

_Explore the knowledge network._

- [[Artificial Intelligence]]
    
- [[Machine Learning]]
    
- [[Neural Networks]]
    
- [[Transformer]]
    
- [[Generative AI]]
    
- [[Token]]