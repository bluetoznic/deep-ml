def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    tokens=corpus.split()
    N=len(tokens)
    count=tokens.count(word)
    return count/N