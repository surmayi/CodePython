def precisionIncrement(num,method):
    if method==1:
        num=int(''.join(map(str,num)))
        num+=1
        return list(str(num))
    else:
        num[-1]+=1
        for i in range(len(num)-1,0,-1):
            if num[i]>=10:
                num[i]=num[i]%10
                num[i-1]+=1
            else:
                break
        if num[0]==10:
            num[0]=1
            num.append(0)
        return num




print(precisionIncrement([9,9,9],1))
print(precisionIncrement([9,9,9,1],2))