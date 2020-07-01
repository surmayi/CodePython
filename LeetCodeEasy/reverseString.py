class Solution(object):
    def reverseString(self, s):
        l= len(s)
        for i in range(l//2):
            temp=s[i]
            s[i]=s[l-i-1]
            s[l-i-1]=temp