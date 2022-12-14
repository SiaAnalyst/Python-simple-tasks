def real_len(text):
    spec_symbols = ['\n', '\f', '\r', '\t', '\v']
    real_text = ''

    for i in text:
        if i not in spec_symbols:
             real_text +=i
    #print(real_text)
    return len(real_text)


text = 'Alex'
real_len(text)