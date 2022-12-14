import re


def replace_spam_words(text, spam_words):
    for i in spam_words:
        text = re.sub(i, '*'*len(i), text, flags = re.IGNORECASE)
    return text