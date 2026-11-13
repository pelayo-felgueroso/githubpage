
--- 
title: "Hello, Welcome to my notes"
---

My name is [[Pelayo Felgueroso]], I like learning by connecting ideas. Whenever I get interested in something, I tend to go down the rabbit hole, take notes, break things down and connect what I'm learning to things I already know.

Over the years, I've built up a collection of notes on all sorts of topics using [[Obsidian]]. I've decided to make them public in the hope that they might be useful to someone else along the way.

You could, of course, just ask ChatGPT, but I think there's something different about exploring a collection of interconnected notes. You might come here looking for one thing, but find other things you didn't even know you needed to learn about.

That's the idea behind this vault: concise, structured and (hopefully) accurate knowledge, with an emphasis on how things fit together.

It's a work in progress, just like my own learning. Feel free to explore.

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
