import re
re_int = re.compile(r'^[+-]?\d+$')
re_float = re.compile(r'^[+-]?(\d*[.])?\d+$')
re_plus_int = re.compile(r'^\d+$')
re_plus_float = re.compile(r'^(\d*[.])?\d+$')

def validator (pattern, prompt):
    var= input(prompt)
    while not bool(pattern.match(var)):
        var= input(prompt)
    return var