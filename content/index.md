---
title: "A collection of things I'm learning about"
---

This is a personal collection of notes on different topics, built up over time. It brings together explanations, practical knowledge, references and connections between ideas. Its purpose is simply to help me understand things better, keep track of what I've learned and have everything in one place to come back to.

The main topics covered include:

- [[Computer Vision]]
    
- [[Image Processing]]
    
- [[Robotics]]
    
- [[Deep Learning]]
    
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


For some information about my background and professional experience, see [[About Me]].
