def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        num = (length - len(string)) // 2
        string = " "*num + string
        return string


print(format_string(string='aaaaaaaaaaaaaaaaac', length=12))
print(format_string(length=15, string='abaa'))