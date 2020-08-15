class Solution(object):
    def letterCombinations(self, digits):
        mapping= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res =[''] if digits else []
        for d in digits:
            cur=list()
            for l in mapping[d]:
                for val in res:
                    cur.append(val+l)
            res=cur
        return res
        
