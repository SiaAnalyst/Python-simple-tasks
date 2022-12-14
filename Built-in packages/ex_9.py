from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)
    return lifo

def pop():
    return lifo.popleft()