class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zero=[]
        i=0
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]==0:
                    zero.append((i,j))
                j+=1
            i+=1
        for (i,j) in zero:
            for r in range(0,n):
                matrix[i][r]=0
            for c in range(0,m):
                matrix[c][j]=0
        
