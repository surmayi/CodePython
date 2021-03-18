def countConsonents(st):
    if not st:
        return 0
    if st[0] not in ['a','e','i','o','u']:
        return 1 + countConsonents(st[1:])
    return countConsonents(st[1:])


print(countConsonents('linearwww'))