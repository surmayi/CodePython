def findStringLength(st):
    if not st:
        return 0
    return 1 + findStringLength(st[1:])


print(findStringLength('123linear'))