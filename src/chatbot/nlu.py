import re

def match(pattern, text):
    m = re.match(pattern, text)
    if m:
        return m.groups()
    return None