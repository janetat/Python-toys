import re

def trim(string):
    return re.sub(r'^(\s+)|(\s+)$', '', string)
