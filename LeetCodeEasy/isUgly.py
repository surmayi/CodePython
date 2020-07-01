class Solution(object):
    def isUgly(self, num):
        if num in [1,0]:
            return num==1
        else:
            for i in [2,3,5]:
                while(num%i==0):
                    num=num//i
            return num==1