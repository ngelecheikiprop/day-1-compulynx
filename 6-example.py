#!/usr/bin/python3
import re
txt="ababaa kiaapabrop"
x = re.findall("(ab)+", txt)
print(x)