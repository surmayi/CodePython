class Solution(object):
    def findWords(self, words):
        first=['q','w','e','r','t','y','u','i','o','p']
        sec=['a','s','d','f','g','h','j','k','l']
        third=['z','x','c','v','b','n','m']
        new=[]
        first.sort()
        sec.sort()
        third.sort()
        for word in words:
            l=len(word)-1
            if word[0].lower() in first:
                templist=first
            elif word[0].lower() in sec:
                templist =sec
            else:
                templist=third
            flag = True
            while(l>0):
                if word[l].lower() not in templist:
                    flag =False
                    break;
                l-=1
            if(flag):
                new.append(word)
        return new
        