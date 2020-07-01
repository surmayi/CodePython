class Solution(object):
    def reverseVowels(self, s):
        vow=[]
        s=list(s)
        for ch in s:
            if ch.isalpha() and ch.lower() in ['a','e','i','o','u']:
                vow.append(ch)
        for i,ch in enumerate(s):
            if ch.isalpha() and ch.lower() in ['a','e','i','o','u']:
                s[i]=vow.pop()
        return ''.join(s)