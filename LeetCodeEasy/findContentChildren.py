class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count=0
        while(len(s)>0):
            if len(g)>0 and s[0]>=g[0]:
                s.pop(0)
                g.pop(0)
                count+=1
            else:
                s.pop(0)
        return count