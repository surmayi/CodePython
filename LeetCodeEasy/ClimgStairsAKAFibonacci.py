def climbStairs( n):
        first=0
        second=1
        if n in [1,2,3]:
            return n
        while(n>0):
            sum1 = first+second
            first=second
            second=sum1
            n-=1
        return second


climbStairs(10)