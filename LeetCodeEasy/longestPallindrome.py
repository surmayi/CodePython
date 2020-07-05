class Solution(object):
    def longestPalindrome(self, s):
        count={}
        for ch in s:
            if(ch in count.keys()):
                count[ch]+=1
            else:
                count[ch]=1
        l =0 
        flag=False
        for key,val in count.items():
            if val%2==0:
                l+=val
            else:
                l=l+ 2*(val//2)
                flag = True
        if flag is True:
            l+=1
        return l