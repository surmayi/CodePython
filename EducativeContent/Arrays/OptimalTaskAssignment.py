def optimalTaskAssignment(num):
    num.sort()
    for i in range(len(num)//2):
        print(num[i],num[~i])

A = [6, 3, 2, 7, 5]
optimalTaskAssignment(A)