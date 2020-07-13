class Solution(object):
    def fib(self, N):
        if N==1:
            return 1
        a=0
        b=1
        c=0
        while(N>=2):
            c=a+b
            a=b
            b=c
            N-=1
        return c