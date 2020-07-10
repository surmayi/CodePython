class Solution(object):
    def constructRectangle(self, area):
        import math
        l = int(math.sqrt(area))
        while(l>0):
            if area%l==0:
                return [area//l,l]
            l-=1
        