class Solution(object):
    def sortedSquares(self, A):
        new=[]
        for i in A:
            new.append(i**2)
        new.sort()
        return new
        