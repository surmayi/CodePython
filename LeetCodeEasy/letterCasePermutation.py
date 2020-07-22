class Solution(object):
    def letterCasePermutation(self, s):
        l =len(s)
        new =[]
        new.append(s)
        for i in range(0,l):
            if s[i].isalpha():
                temp =[]
                for j in range(0,len(new)):
                    temp.append(new[j][0:i]+ s[i].lower()+ new[j][i+1:])
                    temp.append(new[j][0:i]+ s[i].upper()+ new[j][i+1:])
                new=temp
        return new
        