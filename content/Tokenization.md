## Explanation

Tokenization is the process of splitting text into smaller units called [[Token|Tokens]] so that a language model can process it.

A token can represent a complete word, part of a word, punctuation or even a single character. The exact way text is divided depends on the tokenizer used by the model.

For example, common words may be represented by a single token, while uncommon or very long words may be split into several smaller tokens. This allows models to work with a limited vocabulary while still handling a large variety of words.

Before text is passed to a language model, the tokens are converted into numerical IDs. These IDs are then used as input to the model and are processed through its neural network layers.

Tokenization is an important part of natural language processing because it affects how text is represented, how many tokens are needed to process it and how much information fits into a model's [[Context Window]].

Different models can use different tokenizers, so the same sentence does not necessarily produce the same number of tokens in every model.

## Resources

- [Hugging Face – Tokenizers Documentation](https://huggingface.co/docs/transformers/en/tokenizer_summary)
    
- [Hugging Face – NLP Course: Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)
    
- [OpenAI – Tokenizer](https://platform.openai.com/tokenizer)
    
- [Computerphile – Why AI Tokens are so Expensive](https://www.youtube.com/watch?v=-0HRzXk8vlk)
## Related concepts

_Explore the knowledge network._

- [[LLM]]
    
- [[Token]]
    
- [[Transformer]]
    
- [[Embedding]]
    
- [[Context Window]]