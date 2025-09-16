from typing import List

def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result

def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    counts = {}
    first_index = {}
    for i, word in enumerate(words):
        counts[word] = counts.get(word, 0) + 1
        if word not in first_index:
            first_index[word] = i

    # sort by frequency descending, then first occurrence ascending
    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], first_index[w]))
    return sorted_words[:k]

def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    result = []
    for word in words:
        if word in banned:
            result.append("***")
        else:
            result.append(word)
    return result

# ===== Example test =====
if __name__ == "__main__":
    words = ["apple", "banana", "apple", "pear", "banana", "apple"]

    print("Unique words:", unique_words_preserve_order(words))
    print("Top 2 frequent:", top_k_frequent_first_tie(words, 2))
    print("Redacted:", redact_words(words, ["banana"]))
