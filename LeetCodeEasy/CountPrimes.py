def countPrimes(self, n):
        if(n in [0,1,2]):
            return 0
        counter=0
        if(n==3):
            return 1
        stay=True
        for j in range(2,n):
            for i in range(2,j):
                if((i**(j-1))%j !=1):
                    stay=False
                    break
                else:
                    stay=True
            if(stay):
                counter+=1
        return counter

countPrimes(10)