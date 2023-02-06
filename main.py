import string
import random

chars = string.printable
chars = chars.replace("", " ")
lst = chars.split()


# Coding
def coding(m):
    n = len(m)
    if n > 3:
        m = m + m[0]
        m = m[1:]
        for i in range(3):
            m = m + random.choice(lst)
            m = random.choice(lst) + m
    else:
        m = m[::-1]
    return m


# Decoding
def decoding(c):
    if len(c) < 3:
        c = c[::-1]
    else:
        c = c[3:]
        c = c[-len(c):-3]
        c = c[-1] + c
        c = c[:-1]
    return c


message = input("Enter your message: ")
print(f"Coded Message: {coding(message)}")
print(f"Decoded Message: {decoding(coding(message))}")
