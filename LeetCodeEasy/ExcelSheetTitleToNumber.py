import string
def titleToNumber( n):
        dic={}
        for i in range(1,27):
            dic[string.ascii_uppercase[i-1]]=i
        n= list(n)
        l= len(n)-1
        num= dic[n[l]]
        for i in range(1,l+1):
            num= num+ dic[n[i-1]]*26**(l-(i-1))
        return num

titleToNumber(720)