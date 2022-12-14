def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    elif len(s)>=1:
        if s.isdigit():
            return True
        elif s[1:].isdigit():
            return True
    return False