'using groups to take any words that numbers has started'

#!/usr/bin/python3
import re
txt="123kiprop david 11lion"
x = re.findall(r"[0-9]+(\w+)", txt)
print(x)