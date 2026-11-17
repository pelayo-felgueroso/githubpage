## Explanation

The Transformer is a neural network architecture designed to process sequences of data, especially text. It was introduced in the paper _Attention Is All You Need_ in 2017.

Its main feature is the attention mechanism, which allows the model to determine how much importance different parts of the input have when processing each element.

For example, when processing a sentence, the model can use information from other words in the sentence to understand the meaning of a particular word. This helps it capture relationships between words, even when they are far apart.

Unlike earlier sequence models that processed information step by step, Transformers can process many elements of a sequence in parallel during training. This makes them suitable for training large models on extensive datasets.

A Transformer typically uses several layers of attention and feed-forward networks. Depending on its design, it can be used for tasks such as text classification, translation, text generation and image processing.

Transformers are the foundation of many modern [[LLM]]s and other generative AI systems. They are also used beyond language, for example in computer vision and robotics.

## Resources

_Learn more from external sources._

- [Hugging Face – Transformer Models](https://huggingface.co/docs/transformers/en/index)
    
- [The Illustrated Transformer – Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
    
- [Attention Is All You Need – Original Paper](https://arxiv.org/abs/1706.03762)
    
- [Computerphile – AI Language  Models & Transformers](https://www.youtube.com/watch?v=rURRYI66E54)
## Related concepts

_Explore the knowledge network._

- [[Neural Networks]]
    
- [[Deep Learning]]
    
- [[Machine Learning]]
    
- [[LLM]]
    
- [[Tokenization]]
    
- [[Embedding]]
    
- [[Generative AI]]