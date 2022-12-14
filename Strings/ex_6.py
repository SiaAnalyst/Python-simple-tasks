import re
def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    print(text)
    if not space_around:
        for i in spam_words:
            if i in text:
                return True
            else:
                return False
    else:
        result = re.findall(r'\w+', text)
        #print(result)
        for i in spam_words:
            if i in result:
                return True
            else:
                return False