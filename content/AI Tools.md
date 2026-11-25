A Tool is a function given to an [[LLM]] so that an [[Agents|Agent]] can take actions: searching the web, calling an API, running a calculation and so on.

The LLM can't run tools itself, because it only reads and writes text. Instead, it writes a request to use a tool, the agent runs the tool, and the result is passed back to the LLM so it can continue.

Tools are what let agents go beyond text generation: they give the model access to up-to-date information, precise calculations and the outside world.

## Explanation

### What is a tool?

One crucial aspect of AI [[Agents]] is their ability to take actions, and this happens through tools. A tool is a function given to the LLM, and it should fulfil a clear objective.

Some commonly used tools:

|Tool|Description|
|---|---|
|Web search|Fetches up-to-date information from the internet.|
|Image generation|Creates images based on text descriptions.|
|Retrieval|Retrieves information from an external source.|
|API interface|Interacts with an external API (GitHub, YouTube, Spotify, etc.).|

These are only examples: a tool can be created for any use case.

### When is a tool useful?

A good tool complements what the LLM does badly on its own:

- Precise calculations: for arithmetic, a calculator tool gives better results than relying on the model.
- Up-to-date information: an LLM's knowledge only includes what was in its training data. If the agent needs current data, it has to get it through a tool. For example, an LLM asked about today's weather without a search tool may simply invent an answer (hallucinate).

### How do tools work?

LLMs can only receive text and generate text, so they can't call tools on their own. "Giving tools to an agent" means telling the LLM which tools exist and instructing it to write a text request when it needs one.

For example, with a weather tool available and the question "What's the weather in Paris?":

1. The LLM recognises that it should use the weather tool, and instead of answering, it writes a tool call as text.
2. The agent reads this response, sees that a tool call is required and runs the tool on the LLM's behalf, getting the real weather data.
3. The agent adds the result to the conversation as a new message and passes it back to the LLM.
4. The LLM uses this new information to write a natural answer for the user.

These tool-calling steps are usually hidden from the user. From the user's point of view, it looks as if the LLM used the tool directly, but in reality the agent handled the whole process in the background.

## Resources

- [Hugging Face – What are tools?](https://huggingface.co/learn/agents-course/unit1/tools)

## Related concepts

_Explore the knowledge network._

- [[Agents]]
- [[LLM]]
- [[AI model]]