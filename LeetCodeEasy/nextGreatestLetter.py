class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if len(letters)==0:
            return 0
        f=0
        l=len(letters)-1
        result=0
        while f<=l:
            m= f+ (l-f)//2
            if letters[m]>target:
                result =m
                l=m-1
            else:
                f=m+1
        return letters[result] 
        