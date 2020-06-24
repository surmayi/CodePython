def hammingWeight( n):
        n = '{0:032b}'.format(n)
        sum1= sum(1*int(i) for i in n)
        return sum1

hammingWeight(964176192)