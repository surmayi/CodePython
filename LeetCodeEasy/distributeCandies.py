class Solution(object):
    def distributeCandies(self, candies):
        dif =len(set(candies))
        if dif <= len(candies)//2:
            return dif
        else:
            return len(candies)//2