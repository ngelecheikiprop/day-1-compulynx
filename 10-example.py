#!/usr/bin/python3
import re
postal_address="""John Kamau
P.O. Box 12345-00100
Nairobi
Kenya"""
print(postal_address)
x = re.findall(r"P.O.\sBox\s([0-9]+)", postal_address)
print(type(x))
print(x)