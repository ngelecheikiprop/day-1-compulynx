#!/usr/bin/python3
import re

txt = "the rain in spain"
x = re.split(r"ai", txt)
print(type(x))
print(x)
