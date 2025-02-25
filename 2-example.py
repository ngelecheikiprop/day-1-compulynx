#!/usr/bin/python3 
import re

txt = "what a day 1"
x = re.search(r"\d", txt)
print(type(x))
print(x)
