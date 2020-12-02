#!/usr/local/bin/python3

import hashlib
import colored

print(colored.stylize("\n---- | Hash input with sha256 | ----\n", colored.fg("red")))
input = input("Import text: ")
print()

input_encoded = input.encode("utf-8")
print(f"Encoded input string: {input_encoded}")

input_hashed = colored.stylize(hashlib.sha256(input_encoded).hexdigest(), colored.fg("red"))
print(f"Hashed input string: {input_hashed}\n")
