class Solution(object):
    def countPrimes(self, n):
        if n in [0,1]:
            return 0
        indices= [1] *n
        indices[0]=0
        indices[1]=0
        for i in range(2, int(n**0.5)+1):
            if indices!=0:
                indices[i*i:n:i] = [0] * ((n-1-i*i)//i+1)
        return sum(indices)
        