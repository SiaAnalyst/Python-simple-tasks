import re


def find_word(text, word):
    dict = {}
    result = re.search(word, text)
    if result:
        dict['result'] = True
        dict['first_index'] = result.start()
        dict['last_index'] = result.end()
        dict['search_string'] = word
        dict['string'] = text
    else:
        dict['result'] = False
        dict['first_index'] = None
        dict['last_index'] = None
        dict['search_string'] = word
        dict['string'] = text
    #print(dict)
    return dict