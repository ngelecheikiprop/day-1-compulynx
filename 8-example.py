#!/usr/bin/python3
import re
txt="<a> b <c>"
x = re.findall(r"<.*?>", txt)
print(x)