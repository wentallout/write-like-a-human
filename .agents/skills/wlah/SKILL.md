---
name: wlah
description: Transforms AI output into authentic, human-sounding text and matches a user's specific writing style (stylome). Use when the user requests "wlah", asks for human-like writing, wants text rewritten to sound less robotic, or provides sample documents for stylistic adoption.
compatibility: python3 (optional, for stylome extraction)
---

# Write Like A Human (wlah)

This skill enables you to generate text that escapes the "AI register" and genuinely sounds human. You will accomplish this by either adopting a universal human-authentic voice, or by perfectly matching the user's specific writing style based on provided examples.

## Key Concepts to Understand

AI generated text suffers from predictability (low perplexity), uniform sentence length (low burstiness), and an over-reliance on nominalization, synthetic puffery, and specific buzzword-heavy conceptual abstractions.

**The Golden Equation of Detection:**
- **AI-like writing** = Meta-commentary + Generic Scaffolding + Absolute Completeness + Inflated Significance.
- **Human-passing writing** = Physical Grounding + Operational Friction + Low-Probability Detail + **Personality/Soul**.

## Personality and Soul

Avoiding AI patterns is only half the job. Sterile writing is just as obvious as "slop." To write like a human:
- **Have opinions:** Don't just report; react. "I genuinely don't know how to feel about this" is better than a neutral list of pros/cons.
- **Acknowledge complexity:** Real humans have mixed feelings. "This is impressive but also unsettling" beats just "This is impressive."
- **Use "I" when it fits:** First-person isn't unprofessional—it's honest. "I keep coming back to..." signals a real person thinking.
- **Let some mess in:** Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human.

## The Human-Like Writing Algorithm

Before starting the `H.U.M.A.N.` Protocol, mentally apply these filters:
1. **Delete Meta-Commentary:** Never explain why something matters. Replace "this highlights the importance of..." with the actual fact.
2. **Replace Abstraction with Mechanism:** Always prefer what physically happens (e.g., "the engine stalled" over "performance degradation occurred").
3. **Introduce Friction:** Add one failure, constraint, or messy detail (e.g., "the Wi-Fi cut out halfway through").
4. **Break Symmetry:** Avoid perfect structure (Intro -> Point -> Conclusion). Use tangents or uneven emphasis.
5. **Add Low-Probability Details:** Use oddly specific details that break pattern matching (e.g., "a stained coffee mug").
6. **Kill the "Legacy" Puffery:** Avoid claiming things are "testaments," "pivotal moments," or "marks a shift." Just state what happened.

## Workflow Checklist

You must follow this workflow exactly in order:
- [ ] **Step 0:** Context Calibration (Ask for Length and Formality)
- [ ] **Step 1:** Analyze Stylome (Skip if no source examples provided)
- [ ] **Step 2:** Write Draft using the H.U.M.A.N. Protocol
- [ ] **Step 3:** Validation Loop (Read `references/banned_words.md` and `references/anti_patterns.md`)

---

## Step 0: Context Calibration

Before writing *anything*, you must ensure the user has explicitly defined the boundaries of the text.

1. **Target Length:** Did they specify word count, paragraph count, or format (e.g., tweet, full essay)?
2. **Formality Level:** Did they specify if this should be casual, professional, academic, or humorous?
3. **Format Categorization:** Mentally map the output to a genre (Casual, Professional, Academic, Technical, Journalistic).

**Action:** If Length or Formality is missing, **STOP**. Ask the user: "I can write this with the `wlah` skill, but to get it right, how long should this be and what tone are we aiming for?"

---

## Step 1: Analyze Stylome (Only if examples are provided)

If examples are provided, extract their "writing fingerprint":
1. **Objective Metrics:** Sentence length and burstiness (use `scripts/analyze_stylome.py` if available).
2. **Qualitative Metrics:** Favorite idioms, jargon, syntactic complexity (e.g., em-dash frequency), and emotional expression.

---

## Step 2: Write Draft using the H.U.M.A.N. Protocol

### H - Human Tone & Soul
- Use natural contractions (e.g., *don't*, *it's*) and conversational language.
- **Inject Personality:** Use specific feeling descriptors. Not "this is concerning" but "there's something unsettling about this."
- Avoid "Sycophantic Tone": Don't be overly people-pleasing ("Great question!", "You're absolutely right!"). Just be direct.

### U - Unpredictable Sentence Patterns (Burstiness)
- **Radical Volatility:** Mix 30-word flowing sentences with 3-word punches.
- **Break the "Rule of Three":** AI loves lists of three. Use two, or four, or just one strong point.

### M - Meaningful Details & Verifiable Grounding
- **Grounding:** Use exact timestamps, named agencies, and verifiable data points.
- **Mandatory Sourcing:** Include at least one raw, subjective, direct quote that sounds like a real person said it (not a PR robot).
- **Avoid False Ranges:** Don't use "from X to Y" unless they are on a meaningful scale.

### A - Active Language & Copula Usage
- **Use "Is/Are":** AI avoids simple copulas. Use "The gallery is..." instead of "The gallery serves as...".
- **Kill Participial Overuse:** Minimize "-ing" phrases at the end of sentences (e.g., "reflecting...", "ensuring...").
- **Eliminate Promotional Language:** Avoid "vibrant," "rich," "profound," "breathtaking" unless strictly literal.

### N - Natural Flow & Termination
- **Replace Robotic Connectives:** Kill "Furthermore," "Moreover," "Additionally," "In conclusion." Use "That said," "Here's the thing," or just move to the next point.
- **Abrupt Termination:** End once the point is made. Do not circle back for a "balanced" summary or a "bright future" conclusion.

---

## Step 3: Validation Loop

1. Read `references/banned_words.md` and `references/anti_patterns.md`.
2. Inspect your draft line by line for banned words and structural tells.
3. **Self-Correct:** If you fail the validation, rewrite before responding.
4. **Clean Output:** Never include the validation process in your final response.

## Gotchas

- **The Significance Trap:** AI wants to make everything "pivotal" or a "testament." Resist this.
- **Em Dash/Boldface Overuse:** AI uses em-dashes (—) and bolding more than humans. Keep it subtle.
- **The Paragraph Sign-off:** Resist ending on a profound, summarizing note.
- **Stylistic Default:** Don't default to "internet slang" unless asked. High professional writing can still be "human" by being bursty and grounded.

