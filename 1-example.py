#!/usr/bin/python3
'using the search function in re'
import re

txt = "the rain in spain"
x = re.search(r"\s", txt)
print("the first white space chcaracter is located in position:", x.start())
