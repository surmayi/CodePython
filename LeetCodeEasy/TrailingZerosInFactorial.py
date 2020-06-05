def trailingZeroes(n):
    num =1
    while(n>0):
        num = n* num
        n-=1
    print(num)
    num = list(map(int,str(num)))
    counter=0
    while(num[-1]==0):
        counter+=1
        num.pop()
    return counter

trailingZeroes(5)