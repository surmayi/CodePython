class Solution(object):
    def firstUniqChar(self, s):
        s=list(s)
        l =len(s)
        done={}
        order=[]
        for i in range(0,l):
            if s[i] in done.keys():
                done[s[i]]+=1
            else:
                done[s[i]]=1
                order.append(s[i])
        for i in order:
            if done[i]==1:
                return s.index(i)
        return -1