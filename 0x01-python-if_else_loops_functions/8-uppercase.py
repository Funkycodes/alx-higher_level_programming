#!/usr/bin/python3
def uppercase(str):
    cstr = ''
    for char in str:
        if ord(char) in range(97, 123):
            cstr += chr(ord(char) - 32)
        else:
            cstr += char
    print(cstr)
