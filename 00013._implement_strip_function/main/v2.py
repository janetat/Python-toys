def trim(string):
    if not string:
        return

    if string[0] == ' ':
        return trim(string[1:])

    if string[-1] == ' ':
        return trim(string[:-1])

    return string
