import re


def find_all_words(text, word):
    result = re.findall(word, text, flags=re.IGNORECASE)
    return result