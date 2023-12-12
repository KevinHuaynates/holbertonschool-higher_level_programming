#!/usr/bin/python3
import dis
with open("hidden_4.pyc", "rb") as f:
    code = f.read()
dis.dis(code)
