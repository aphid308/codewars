import re
import string


def decrypt(code):
    translator = dict(enumerate(string.ascii_lowercase, 1))
    translator[0] = " "
    code_digits = [re.sub("[^0-9]", "", x) for x in code.split(' ')]
    code_sums = []
    
    for e in code_digits:
        code_sums.append(sum([int(x) for x in e]))

    message = ""

    for i in code_sums:
        if i > 26:
            i = i % 27
        message += translator[i]

    return message









print(decrypt('x20*6<xY y875_r97L'))
