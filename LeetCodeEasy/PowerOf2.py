def isPowerOfTwo( n):
        while(n>1):
            n=float(n)/2
            print(n)
            if(n!=int(n)):
                return False
        if(n==1):
            return True
        return False