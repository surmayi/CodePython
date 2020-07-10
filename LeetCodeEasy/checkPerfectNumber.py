class Solution(object):
    def checkPerfectNumber(self, num):
        if num <=1:
            return False
        sum1 =set([1])
        for i in range(2,int(num**0.5) +1):
            if num%i==0:
                sum1.add(i)
                sum1.add(num/i)
        if sum(sum1)==num:
            return True
        return False
        