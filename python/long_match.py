# find the longest substring that matches a given regex
def getLongMatch(text: str, regex: str):
    # text = hackerrank, regex = `ack*r`, longest is `ackerr`

    # can have only 1 asterisk
    if len(regex) == 1:
        return text
    start = regex.index("*")

    prefix = regex[0:start]
    suffix = regex[(start + 1) :]
    idx = -1

    if prefix and len(prefix) > 0:
        idx = text.find(prefix)
    else:
        idx = 0

    last_idx = -1
    if suffix and len(suffix) > 0:
        last_idx = text.rfind(regex)
    else:
        last_idx = len(text)

    if idx < 0 or last_idx < 0:
        return -1

    if idx + len(prefix) > last_idx:
        return -1

    return last_idx + len(suffix) - idx
