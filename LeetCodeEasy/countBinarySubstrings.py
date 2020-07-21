class Solution(object):
    def countBinarySubstrings(self, s):
        if '0' not in s or '1' not in s:
            return 0
        s = s.replace('10', '1 0')
        s = s.replace('01', '0 1')
        l =s.split(' ')
        count=0
        for i in range(len(l)-1):
            count = count+ min(len(l[i]),len(l[i+1]))
        return count
        