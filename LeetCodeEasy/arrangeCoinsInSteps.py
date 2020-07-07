class Solution(object):
    def arrangeCoins(self, n):
        prevcount=0
        count=1
        while(n>=0):
            n=n-count
            prevcount+=1
            count+=1
        return prevcount-1