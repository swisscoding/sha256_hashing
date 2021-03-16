#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import hashlib

# decoration
print(stylize("\n---- | Hash input with sha256 | ----\n", fg("red")))

# user interaction
input = input("Import text: ")

# function
def hash(s):
    # encode
    input_encoded = s.encode("utf-8")
    print(f"\nEncoded input string: {input_encoded}")

    input_hashed = stylize(hashlib.sha256(input_encoded).hexdigest(), fg("red"))
    return f"\nHashed input string: {input_hashed}\n"

# output
print(hash(input))
