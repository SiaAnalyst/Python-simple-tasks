# CESAR'S CODE

import string

message = input("Enter message: ")
offset = int(input("Enter offset: "))
encoded_message = ""
for ch in message:
    if ch in string.ascii_letters:
        if ch == ch.upper():
            pos = ord(ch) - ord('A')
            pos = (pos + offset) % 26
            new_char = chr(pos + ord("A"))
        else:
            pos = ord(ch) - ord('a')
            pos = (pos + offset) % 26
            new_char = chr(pos + ord("a"))
        encoded_message += new_char
    else:
        encoded_message += ch
print(encoded_message)