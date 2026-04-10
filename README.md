# Write Like A Human (WLAH)

**Strip the machine, keep the mess.**

---

### What is WLAH?

AI is too perfect. It’s clear, it’s structured, and it’s boring. Humans are the opposite—we’re messy, opinionated, and we get oddly specific about things that don't matter.

WLAH breaks the "AI writing style" by:

- **Killing the fluff.** If a sentence exists just to explain the _next_ sentence, it's gone. No more "In conclusion" or "Furthermore."
- **Adding friction.** Real life is full of broken gear and bad Wi-Fi. We inject those details to ground the writing.
- **Breaking the rhythm.** AI loves even sentence lengths. We mix long, flowing thoughts with short punches.

---

### How to Install

You can add WLAH to your project using the one-command installer:

```bash
npx skills add wentallout/write-like-a-human --skill wlah
```

**Manual Installation:**
1. Clone this repository.
2. Copy the `.agents/skills/wlah` directory into your project's `.agents/skills/` folder.

---

### How to Use

Simply include the keyword **`wlah`** in your prompt. For the best results, define your intended **length** and **tone**.

**Example Prompt:**

> "Review this React component using **wlah**. Keep it under 200 words and make it sound like a frustrated senior dev."

### Professional Grade: Your Personal Stylome

WLAH is most effective when it learns _how you talk_. You can prime the model by providing samples of your own writing.

**Example Prompt:**

> "I'm going to provide 3 samples of my personal blog posts. First, analyze my **stylome** (my rhythm, favorite quirks, and tone). Then, use **wlah** to write a new post about [Topic] using my exact voice."

---

### Before vs. After

| **Standard AI**                                                                                                                        | **WLAH Humanized**                                                                                          |
| :------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| "It is important to note that coffee cultivation is a complex process. Furthermore, the aroma is often described as rich and vibrant." | "Coffee is a pain to grow. My first batch smelled like burnt rubber and regret, but at least it felt real." |

---

### Shortcuts

- **[wlah/SKILL.md](.agents/skills/wlah/SKILL.md)**: The core H.U.M.A.N protocol.
- **[references/](.agents/skills/wlah/references/)**: Lists of banned "AI words" and structural anti-patterns.
- **[analyze_stylome.py](.agents/skills/wlah/scripts/analyze_stylome.py)**: The script used to extract stylistic metrics.

---

### Credits & Citations

- **Wikipedia Field Guide:** Logic for our blocklists and anti-patterns comes from the [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) community guide.
- **The Human Stylome:** Our focus on linguistic volatility is inspired by research into the ["human stylome"](https://www.tandfonline.com/doi/abs/10.1080/09296170500055350) (Van Halteren et al., 2005).
- **Personality Modeling:** Techniques for injecting soul into prose are informed by the [PERSONAGE system](https://cljournal.org/archives/v37/v37n3.pdf) (Mairesse & Walker, 2011).
- **Machine-in-the-Loop:** Our philosophy on human-agent collaboration draws from [Creative Writing with a Machine in the Loop](https://arxiv.org/abs/1801.10181) (Clark et al., 2018).
