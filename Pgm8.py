import re

def check(s):
    pattern = re.compile(r'^[a-zA-Z0-9 ]+$')
    return bool(pattern.match(s))

print(check("CT 2025"))
print(check("CT_2025"))
print(check("2025"))
print(check("CE department"))
