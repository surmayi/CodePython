class Solution(object):
    def compress(self, chars):
        l = len(chars)
        i=0
        n=[]
        while(i<l):
            key=chars[i]
            val=1
            while i<l-1 and chars[i]==chars[i+1]:
                val+=1
                i+=1
            i=i+1
            n.append(key)
            if(val>1):
                val = str(val)
                for j in range(len(val)):
                    n.append(str(val[j]))
        nl=len(n)
        i=0
        while(i<nl):
            chars[i]=n[i]
            i+=1
        return nl
        