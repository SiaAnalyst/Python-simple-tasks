import re

def capital_text(s):
    p = re.compile(r'(?<=[\.\?!]\s)(\w+)')
    s = s.capitalize()
    def cap(match):
        return(match.group().capitalize())

    return p.sub(cap, s)