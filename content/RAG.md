## Explanation

One problem with [[LLM]]s is that they don't automatically know everything about your documents or the information you want them to use. They generate answers based on what they learned during training and the context you give them.

**RAG (Retrieval-Augmented Generation)** is a way to give an LLM access to external information when answering a question.

The idea is quite simple: before generating an answer, the system searches for relevant information in a collection of documents and passes the results to the model as additional context.

For example, imagine you have hundreds of technical documents and want to ask questions about them. Instead of expecting the LLM to know what's inside every document, a RAG system first looks for the relevant sections and then uses them to generate an answer.

This usually involves splitting documents into smaller chunks, creating [[Embedding]]s for them, storing them in a [[Vector Database]] and retrieving the most relevant ones when a question comes in.

## Resources

_Learn more from external sources._

## Related concepts

_Explore the knowledge network._

- [[LLM]]
    
- [[Embedding]]
    
- [[Vector Database]]
    
- [[Semantic Search]]
    
- [[Token]]
    
- [[Context Window]]