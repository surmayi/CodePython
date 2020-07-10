class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
        flag = False
        if num<0:
            flag =True
            num=num*-1
        ans=''
        while(num>0):
            r= num%7
            num=num//7
            ans=str(r) + ans
        if(flag):
            ans ='-'+ans
        return ans
        