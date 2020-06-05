def countAndSay(n):
    vals=[1]
    for i in range(1,n):
        prev = vals[-1]
        prev = list(map(int, str(prev)))
        temp ={}
        ind=0
        j=0
        while(j<len(prev)):
            v = prev[j]
            temp[ind] = [1,v]
            j+=1
            while(j<len(prev) and (v==prev[j])):
                temp[ind][0]+=1
                j+=1
            ind+=1
        newval=""
        for key,val in temp.items():
            newval+=str(val[0])+str(val[1])
        vals.append(newval)
    return str(vals[-1])

countAndSay(6)