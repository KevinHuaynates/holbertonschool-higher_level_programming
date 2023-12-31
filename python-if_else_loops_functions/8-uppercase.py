#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase letter to uppercase using ASCII values
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            # Print the character as is if it's not a lowercase letter
            print(char, end='')

    # Print a new line at the end
    print()


# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
