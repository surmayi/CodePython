import string
def convertToTitle( n):
        dic={}
        dic[0]='Z'
        for i in range(1,26):
            dic[i] = string.ascii_uppercase[i-1]
        val=''
        d=0
        if(n<26):
            return str(dic[n])
        if(n==26):
            return 'Z'
        while(n>0):
            d=n%26
            n=n//26
            val=str(dic[d])+val
            if(d==0):
                 n=n-1
        return val

convertToTitle(701)
convertToTitle(720)
convertToTitle(52)