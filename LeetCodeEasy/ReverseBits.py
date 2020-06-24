def reverseBits(n):
    n='{0:032b}'.format(n)
    sum1 = sum(int(i)*2**(id) for id,i in enumerate(n))
    return sum1

reverseBits(964176192)