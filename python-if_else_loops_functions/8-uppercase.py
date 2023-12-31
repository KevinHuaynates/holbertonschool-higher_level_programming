#!/usr/bin/python3

def uppercase(s):
    result = ""
    count = 0

    if isinstance(s, str):
        for char in s:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - ord('a') + ord('A'))
            else:
                result += char
            count += 1

    print("{}".format(result), end='\n' if count > 0 else '')
