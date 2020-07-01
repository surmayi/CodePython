class Solution(object):
    def addDigits(self, num):
        if num<10:
            return num
        else:
            temp=0
            while(num>0):
                d=num%10
                num=num//10
                temp=temp+d
            return self.addDigits(temp)