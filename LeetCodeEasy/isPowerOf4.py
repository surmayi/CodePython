class Solution(object):
    def isPowerOfFour(self, num):
        if num<=0:
            return False
        while(num>1):
            if num%4 !=0:
                return False
            num=num//4
        return True