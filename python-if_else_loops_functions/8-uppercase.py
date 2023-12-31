#!/usr/bin/python3


def uppercase(s):
    result = ""
    count = 0
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
        count += 1

    print(result, end='\n' if count > 0 else '')


# Test cases
uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase(98)
uppercase('z')
