# AI Writing Detection Benchmarks & Testing Resources

To evaluate the effectiveness of the `wlah` skill in producing human-like, non-detectable text, you should test it against both **live commercial detectors** and **scientific benchmarks**.

## 1. Live Commercial Detectors (Practical Tests)
These are the primary tools used by educators, publishers, and SEO professionals. Success here is the most "real-world" validation for `wlah`.

| Tool | Focus Area | Access |
| :--- | :--- | :--- |
| **[GPTZero](https://gptzero.me/)** | Education & Academic Integrity | Free/Paid (Web Interface) |
| **[Originality.ai](https://originality.ai/)** | SEO, Content Marketing, Publishers | Paid (API & Web) |
| **[Copyleaks](https://copyleaks.com/ai-content-detector)** | Institutional & Enterprise | Free/Paid (Chrome Ext/Web) |
| **[Winston AI](https://gowinston.ai/)** | Publishers & Educators | Free/Paid (High Accuracy) |
| **[QuillBot AI Detector](https://quillbot.com/ai-content-detector)** | General Writing/Editing | Free (Sentence-level breakdown) |

> [!TIP]
> **Originality.ai** and **GPTZero** are currently considered the "gold standards" for high-sensitivity detection. If `wlah` can consistently score <10% AI on these, it is highly effective.

## 2. Academic Benchmarks (Scientific Datasets)
If you want to perform more rigorous, large-scale testing (e.g., using a test suite of 100+ documents), these are the standard datasets used in AI research.

*   **RAID (Robust AI Detection):** Currently one of the most comprehensive benchmarks. It includes 10 million documents and specifically tests against **paraphrasing and adversarial attacks**.
*   **PADBen (Paraphrase Attack Detection Benchmark):** Specifically designed to measure how well detectors hold up against "laundering" (iterative paraphrasing to hide AI origins).
*   **[HC3 (Human-ChatGPT Comparison Corpus)](https://huggingface.co/datasets/Hello-SimpleAI/HC3):** A foundational dataset for comparing human vs. AI stylistic features.
*   **MGTBench:** A benchmarking framework for modern LLMs like GPT-4 and Claude 3.5.

## 3. Recommended Testing Strategy for WLAH
To scientifically prove `wlah` works, follow this A/B workflow:

1. **Control:** Generate raw text from GPT-4o/Claude.
2. **Experiment:** Apply `wlah` to the same prompt.
3. **Compare:** Run both through detectors and check **Perplexity** and **Burstiness**.

## 4. Key Metrics to Monitor
*   **Perplexity:** Complexity of word choice (Human = High).
*   **Burstiness:** Variation in sentence structure (Human = High).
*   **AI Connectors:** Avoid "Furthermore", "In conclusion", "It is important to note".
