class Solution(object):
    def maxProfit(self, prices):
        max1, min1 = 0, float('inf')
        for val in prices:
            if val<min1:
                min1=val
            diff = val-min1
            if max1< val-min1:
                max1=val-min1
        return max1
        