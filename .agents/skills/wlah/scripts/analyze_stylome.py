import sys
import re
import math
import collections

def analyze_text(text):
    # Basic cleaning
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split into sentences (rudimentary but works for our stylome analysis)
    # Splitting on ., !, ? followed by space or end of string
    sentences_raw = re.split(r'[.!?]+(?=\s|$)', text)
    sentences = [s.strip() for s in sentences_raw if s.strip()]
    
    if not sentences:
        print("Error: No valid sentences found in text.")
        return

    # Word counts per sentence
    sentence_lengths = []
    total_words = 0
    all_words = []
    
    for s in sentences:
        words = re.findall(r'\b\w+\b', s.lower())
        word_count = len(words)
        if word_count > 0:
            sentence_lengths.append(word_count)
            total_words += word_count
            all_words.extend(words)

    if not sentence_lengths:
        print("Error: Could not extract words from sentences.")
        return

    num_sentences = len(sentence_lengths)
    
    # Average Sentence Length
    mean_length = total_words / num_sentences

    # Burstiness (Standard Deviation of Sentence Lengths)
    # Higher std_dev means higher burstiness (mix of long and short)
    variance = sum((x - mean_length) ** 2 for x in sentence_lengths) / num_sentences
    std_dev = math.sqrt(variance)

    # Lexical Diversity (Type-Token Ratio)
    unique_words = len(set(all_words))
    lexical_diversity = unique_words / total_words if total_words > 0 else 0

    print("================ STYLOME ANALYSIS ================")
    print(f"Total Sentences Analyzed: {num_sentences}")
    print(f"Total Words Analyzed: {total_words}")
    print("-" * 50)
    print(f"Average Sentence Length: {mean_length:.2f} words (Target this average overall)")
    print(f"Burstiness (Sentence Length Std Dev): {std_dev:.2f} (Higher means more volatile length)")
    print(f"Lexical Diversity (Type-Token Ratio): {lexical_diversity:.2f} (1.0 = all unique words)")
    print("-" * 50)
    
    # Determine profile
    burst_desc = "HIGH (Authentic Human Variation)" if std_dev > 6.0 else "LOW (Robotic/Statistically Safe)"
    print(f"Burstiness Profile: {burst_desc}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_stylome.py <path_to_txt_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        analyze_text(content)
    except Exception as e:
        print(f"Failed to read file: {e}")
