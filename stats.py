from collections import defaultdict

def count_words(text: str) -> int:
    return len(text.split())
    
def count_chars(text: str) -> dict:
    ch_dict = defaultdict(int)
    for ch in text:
        ch_dict[ch.lower()] += 1
    return ch_dict