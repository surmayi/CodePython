class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        l=len(t)-1
        for ch in s:
            if i>l:
                return False
            while i<=l and t[i]!=ch:
                t=t[0:i]+t[i+1:]
                l=l-1
            i=i+1
        if s in t:
            return True
        return False