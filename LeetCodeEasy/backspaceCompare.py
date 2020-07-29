class Solution(object):
    def backspaceCompare(self, S, T):
        from functools import reduce
        def back(res, c):
            if c == '#':
                return res[:-1] 
            else:
                return res + c
        return reduce(back, S, "") == reduce(back, T, "")
        