#!/usr/bin/python3
import re
txt = "age26 phone07572545736 count3"
x = re.findall(r"phone(\d+)", txt)
print(x)