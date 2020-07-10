class Solution(object):
    def hammingDistance(self, x, y):
        lim=0
        if x>y:
            lim=x
        else:
            lim=y
        count=0
        while(lim>0):
            if x%2 !=y%2:
                count+=1
            x=x//2
            y=y//2
            lim=lim//2
        return count
        