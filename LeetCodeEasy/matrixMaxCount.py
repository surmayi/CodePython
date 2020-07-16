class Solution(object):
    def maxCount(self, m, n, ops):
        if len(ops)==1:
            return ops[0][0]*ops[0][1]
        if len(ops) ==0:
            return m*n
        a = min(a[0] for a in ops)
        b = min(b[1] for b in ops)
        return a*b
        