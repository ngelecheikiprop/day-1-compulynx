#!/usr/bin/python3
import re
txt="I am the king"
x = re.findall(r"\w+?", txt)
print(x)