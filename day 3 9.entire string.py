import re

p = "a*"
s = "aa"

p = r"{}".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")
