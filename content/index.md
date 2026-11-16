---
title: "A collection of things I'm learning about"
---

My name is Pelayo Felgueroso. This is a collection of notes I've built up over the years on all sorts of topics, using Obsidian to keep everything organised and connected.

Of course, you could just ask ChatGPT or another [[LLM]] whenever you forget something. But I don't really like having to do that every time and getting a different answer each time.

When I finally understand a concept after spending time researching it, I want to keep that explanation, along with the other ideas that helped me get there. That way, when I come back to it months later, I don't have to spend another hour researching everything just to pick up where I left off.

Remembering things is only part of learning. What really matters is understanding how ideas fit together and being able to use what you've learned to think about new things. Learning techniques like the [[PACER Method]] can help with this by offering different ways to process and remember different types of information, rather than simply memorising facts.

It's a work in progress. Feel free to explore.

If you'd like to know more [[About Me]], you can find a bit more about my background, career and projects.

<div style="margin: 25px 0;">
  <button
    id="random-note-button"
    style="
      padding: 12px 22px;
      border: 1px solid var(--secondary);
      border-radius: 8px;
      background: var(--secondary);
      color: white;
      font-size: 1rem;
      cursor: pointer;
    "
  >
    Take me to a random note
  </button>
</div>

<script>
(() => {
  const button = document.getElementById("random-note-button");
  if (!button) return;

  button.addEventListener("click", async () => {
    button.disabled = true;
    button.textContent = "Finding a note...";

    try {
      const response = await fetch(
        new URL("static/contentIndex.json", window.location.href)
      );

      if (!response.ok) {
        throw new Error("Could not load the content index");
      }

      const index = await response.json();

      const notes = Object.values(index).filter(note =>
        note.slug &&
        note.slug !== "index" &&
        note.slug !== "tags/index" &&
        note.content?.trim().length > 0
      );

      if (notes.length === 0) {
        throw new Error("No notes available");
      }

      const randomNote = notes[
        Math.floor(Math.random() * notes.length)
      ];

      window.location.href = new URL(
        randomNote.slug,
        window.location.href
      ).href;

    } catch (error) {
      console.error(error);
      button.disabled = false;
      button.textContent = "Try again";
    }
  });
})();
</script>
