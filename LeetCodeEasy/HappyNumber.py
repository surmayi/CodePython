def isHappy( n):
        t=0
        k=0
        while(t!=1):
            t=0
            while(n>0):
                m = n%10
                t=t+ m**2
                n=n//10
            if t==1:
                return True
            else:
                n=t
                if(k>100):
                    return False
            k+=1

isHappy(19)