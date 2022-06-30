#!/bin/usr/python3
def remove_char_at(str, n):
    strcopy = ''
    for i in range(len(str)):
        if i == n:
            continue
        strcopy += str[i]
    return strcopy
