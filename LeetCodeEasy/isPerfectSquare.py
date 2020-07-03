class Solution(object):
    def isPerfectSquare(self, num):
        f=num**0.5
        if f == int(f):
            return True
        return False