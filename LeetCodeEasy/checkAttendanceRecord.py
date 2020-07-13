class Solution(object):
    def checkRecord(self, s):
        if len(s) in [0,1]:
            return True
        if 'LLL' in s:
            return False
        s=list(s)
        s.sort()
        if s[0]=='A' and s[1]=='A':
            return False
        return True