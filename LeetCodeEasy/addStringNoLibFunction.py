class Solution(object):
    def addStrings(self, num1, num2):
        l1=len(num1)
        l2=len(num2)
        d = l1-l2
        if d==0:
            pass
        elif d<0:
            num1 = -d*'0' + num1
        else:
            num2 = d*'0' +num2
        l1 = l2 = len(num2)
        newnum=''
        c=0
        for i in range(l1-1,-1,-1):
            t = c+int(num1[i])+int(num2[i])
            if int(t)>=10:
                c=int(str(t)[0])
                newnum= str(t)[1]+ newnum
            else:
                c=0
                newnum= str(t)+ newnum
        if c>0:
            newnum = str(c)+newnum
        return newnum
        