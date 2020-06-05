def reverse( x):
        flag =False
        if x<0:
            flag=True
            x=x*-1
            print(x)
        n=0
        while(x>0):
            n=n*10 + x%10
            x =int(x)/10
        if flag:
            print("Here",n*-1)
            return n*-1*(abs(n)<0x7FFFFFFF)
        else:
            print("Not here",n)
            return n*(abs(n)<0x7FFFFFFF)

reverse(-123)
reverse(120)