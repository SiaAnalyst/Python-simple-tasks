def sequence_buttons(string):
    dict = {
        '1':'.,?!:',
        '2':'ABC',
        '3':'DEF',
        '4':'GHI',
        '5':'JKL',
        '6':'MNO',
        '7':'PQRS',
        '8':'TUV',
        '9':'WXYZ',
        '0': ' '}
    string = string.upper()
    result = ''
    for i in string:
        for j in dict.values():
            if i in j:
                count = j.index(i)+1
                for k, v in dict.items():
                    if v == j:
                        result += k*count
    return result