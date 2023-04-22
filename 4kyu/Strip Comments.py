def strip_comments(strng: str, markers: list):
    value = strng.split('\n')
    for s in markers:
        value = [v.split(s)[0].rstrip() for v in value]
    return '\n'.join(value)


print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))