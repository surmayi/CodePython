class Solution(object):
    def findTheDifference(self, s, t):
        t=list(t)
        for ch in s:
            t.remove(ch)
        return t[0]