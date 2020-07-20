class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        delcount=0
        while(i<len(numbers)):
            n = numbers[i]

            if target-n in numbers[i+1:]:
                return [i+1+ delcount,delcount+i+1+numbers[i+1:].index(target-n)+1]
            else:
                while(n in numbers):
                    delcount+=1
                    numbers.remove(n)
        return [0]
        