class Solution(object):
    def fizzBuzz(self, n):
        lis=[]
        for i in range(1,n+1):
            if i%3 ==0 and i%5==0:
                lis.append('FizzBuzz')
            elif i%3==0:
                lis.append('Fizz')
            elif i%5==0:
                lis.append('Buzz')
            else:
                lis.append(str(i))
        return lis