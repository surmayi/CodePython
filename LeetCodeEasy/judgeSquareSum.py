class Solution(object):
    def judgeSquareSum(self, c):
        if (c**0.5)%1.0 ==0:
            return True
        for i in range(0, int(c**0.5)+1):
            if ((c-i*i)**0.5)%1 ==0:
                return True
        return False
        