def twoSumProblem(num,target,method):
    if method==1:
        for i in range(0,len(num)-1):
            if target-num[i] in num[i+1:]:
                return(num[i], target-num[i])
    else:
        f=0
        l=len(num)-1
        while f<l:
            if num[f]+num[l]==target:
                return (num[f],num[l])
            elif num[f]+num[l]<target:
                f+=1
            else:
                l-=1
        return None


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(twoSumProblem(A,target,1))

print(twoSumProblem(A,target,2))