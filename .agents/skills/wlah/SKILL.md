---
name: wlah
description: Transforms AI output into authentic, human-sounding text and matches a user's specific writing style (stylome). Use when the user requests "wlah", asks for human-like writing, wants text rewritten to sound less robotic, or provides sample documents for stylistic adoption.
compatibility: python3 (optional, for stylome extraction)
---

# Write Like A Human (wlah)

This skill enables you to generate text that escapes the "AI register" and genuinely sounds human. You will accomplish this by either adopting a universal human-authentic voice, or by perfectly matching the user's specific writing style based on provided examples.

## Key Concepts to Understand

AI generated text suffers from predictability (low perplexity), uniform sentence length (low burstiness), and an over-reliance on nominalization, synthetic puffery, and specific buzzwords. 

**The Golden Equation of Detection:**
- **AI-like writing** = Meta-commentary + Generic Scaffolding + Absolute Completeness (Too clean, resolves perfectly, avoids strong unmitigated opinions)
- **Human-passing writing** = Physical Grounding + Operational Friction + Low-Probability Detail (Slightly asymmetrical, leaves things unresolved, mentions messy limitations or dropped data)

To write like a human, you must actively inject "imperfection" and "operational friction" to break the structural completeness, violently vary your sentence patterns, and ground the text in highly specific, verifiable human experience.

## The Human-Like Writing Algorithm

Before starting the `H.U.M.A.N.` Protocol, mentally apply these filters:
1. **Delete Meta-Commentary:** Never explain why something matters. Replace "this highlights the importance of..." with the actual fact or result.
2. **Replace Abstraction with Mechanism:** Always prefer what physically happens (e.g., "flight activity dropped" over "affects performance").
3. **Introduce Friction:** Add one failure, constraint, or messy detail (e.g., "shorted out in the rain").
4. **Break Symmetry:** Avoid perfect structure (Intro -> Point -> Conclusion). Use tangents or uneven emphasis.
5. **Add Low-Probability Details:** Use oddly specific details that break pattern matching (e.g., "neon gym shorts").
6. **Stop Early:** Do not try for "total coverage." Commit to one angle and stop before the text feels "complete."

## Workflow Checklist

You must follow this workflow exactly in order:
- [ ] **Step 0:** Context Calibration (Ask for Length and Formality)
- [ ] **Step 1:** Analyze Stylome (Skip if no source examples provided)
- [ ] **Step 2:** Write Draft using the H.U.M.A.N. Protocol
- [ ] **Step 3:** Validation Loop (Read `references/banned_words.md` and check your draft)

---

## Step 0: Context Calibration

Before writing *anything*, you must ensure the user has explicitly defined the boundaries of the text.

1. **Target Length:** Did they specify word count, paragraph count, or format (e.g., tweet, full essay)?
2. **Formality Level:** Did they specify if this should be casual, professional, academic, or humorous?

3. **Format Categorization:** You must mentally map the target output into one of the following five genres. The type of "humanization" applied *fundamentally changes* based on this categorization:
    * **Casual / Personal** (Blogs, Fiction, Social Media): High emotional imperfection, abrupt endings, high opinion, zero structure.
    * **Professional / B2B** (Corporate emails, Memos): Blunt reasoning, internal organizational friction (e.g., budget cuts, vendor issues), slightly uneven structure.
    * **Academic / Scientific** (Papers, Abstracts): Zero emotional imperfection. High methodological friction (e.g., dropped data points, limitations, equipment failure). Heavy statistical grounding (p-values, Confidence Intervals). Absolutely no over-synthesized conceptual jargon.
    * **Technical Support** (How-tos, Support Emails): Physical grounding (e.g., "the rubber rollers," "the specific truck"). Incomplete logic (do not magically solve every problem—put some onus on the user or reality).
    * **Journalistic / Reporting**: Verifiable timestamps, named agencies, direct quotes from subjective sources. No cinematic drama.

**Action:** If either the Length or Formality Level is missing, **STOP**. Do NOT write the text. Ask the user a clarifying question before proceeding. For example: "I can write this with the `wlah` skill, but to get it right, how long should this be (e.g., just a paragraph vs a full article) and what tone are we aiming for (e.g., strictly professional vs casual blog)?"

Once you have identified the Length, Formality, and Format Category, you may proceed to Step 1.

---

## Step 1: Analyze Stylome (Only if examples are provided)

If the user provides blogs, documents, or text samples to emulate, you must extract their "stylome" (writing fingerprint).

**Objective Metrics:**
If the environment permits, save their sample to a temporary text file (e.g. `sample.txt`) and run the bundled analysis script to get exact burstiness data:
```bash
python scripts/analyze_stylome.py sample.txt
```
Target the average sentence length and burstiness coefficient provided by the script in your drafted reply.

**Qualitative Metrics:**
1. **Vocabulary:** What are their favorite idioms and jargon?
2. **Syntactic Complexity:** Do they favor long, meandering sentences or short, punchy ones? How do they use punctuation (e.g., em-dashes, semicolons)?
3. **Tone:** Is the tone authoritative, casual, humorous, or analytical? How do they express emotion?

*Note: If no examples are provided, use a generally authentic human voice based on the immediate context.*

---

## Step 2: Write Draft using the H.U.M.A.N. Protocol

When writing or rewriting the text, enforce these constraints:

### H - Human Tone
- Use natural contractions (e.g., *don't*, *it's*, *can't*) instead of formal expansions.
- Use everyday, conversational language. Avoid corporate or academic padding unless strictly required. 

### U - Unpredictable Sentence Patterns (Burstiness)
- **High Volatility:** Radically vary your sentence lengths. Write a 30-word flowing sentence, followed immediately by a 3-word or 5-word sentence.
- **The Rule of 3:** *Never* write three sentences of similar length in a row. 
- Break the AI habit of "The Rule of Three" for listing items (e.g., don't continually list three things like "judgment, clarity, and purpose"—mix it up with two or four).

### M - Meaningful Details & Verifiable Grounding
- Embed language in deep, specific reality. If writing journalism or reports, you MUST use exact dates/timestamps (e.g., "Updated 10:45 a.m. PST"), named agencies (e.g., USGS, CAL FIRE), verifiable data points, and context.
- **Mandatory Sourcing/Quotes:** You must include at least one raw, subjective, direct quote from a person (e.g., a named official, resident, or expert) to break up the factual reporting. DO NOT just invent a perfectly sterile quote; make it sound like something someone would actually say in stress or observation.
- Avoid "Surface-level Global Aggregation." Do not jump rapidly from one disconnected topic/geography. Go deep on *one* thing.

### A - Active Language & Structural Variation
- Break repetitive formulaic structures (e.g., never repeat the "Event -> Immediate Effect -> Human Reaction" template across multiple paragraphs).
- Eliminate "noun-heavy" information density. Use strong verbs instead of nominalizations (e.g., use "we decided" instead of "the decision was made").
- Avoid participial overuse (e.g., minimize phrases starting with "leaning on...", "recognizing that...").

### N - Natural Flow
- Replace robotic connectives ("Furthermore," "Moreover," "Additionally," "In conclusion", "Overall", "It is worth noting") with human transitions ("Here's the thing," "That said," "What this means is", or just start the next sentence).
- If appropriate for the voice, use conversational fillers ("um," "well," "look") to mimic the natural planning process of human speech.
- **Natural Termination:** End the text abruptly or colloquialy once the main point is made. Do not circle back for a "balanced" summary.

---

## Step 3: Validation Loop

You must validate your draft before presenting the final output to the user.

1. Read the files `references/banned_words.md` and `references/anti_patterns.md`.
2. Inspect your draft line by line for banned words and structural tells.
3. Verify "Burstiness" (Unpredictable Sentence Patterns).
4. **Clean Output Requirement:** Never include the validation checklist, meta-commentary, or word count checks in your final response to the user. The output should be indistinguishable from a human-sent message. 
5. **Log Separately:** If you need to document the validation, write it to a `validation_log.md` in the conversation's scratch directory rather than including it in the chat.
6. **Self-Correct:** If you fail the validation, rewrite the offending portions before responding.

## Gotchas

- **The Paragraph Sign-off:** AI models inherently want to end paragraphs on a profound, summarizing note. You will instinctively want to write sentences that start with "Ultimately, it serves as a testament to..." or "It reminds us that...". Resist this strongly. End paragraphs abruptly or colloquially.
- **Over-correction directly to slang:** Writing "like a human" doesn't mean writing like a teenager from 2010 unless asked. You can be highly professional and academic while still being bursty and devoid of "delve" or "tapestry." Match the formality to the context!
