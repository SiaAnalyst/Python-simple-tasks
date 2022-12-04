# random password

from random import randint


def get_random_password():
    password = ''
    while len(password) < 8:
        random_num = randint(40, 126)
        password += str(chr(random_num))
    return password