class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        i=0
        for word in s:
            s[i] = word[::-1]
            i+=1
        return ' '.join(s)
        