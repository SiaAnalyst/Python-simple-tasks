# parse args
import sys


def parse_args():
    result = ""
    for i in sys.argv[1:2]:
        result += i
    for i in sys.argv[2:]:
        result += ' ' + i
    return result