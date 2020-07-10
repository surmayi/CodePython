class Solution(object):
    def repeatedSubstringPattern(self, s):
        ss=s[0]
        s=s[1:]
        while(len(s)>=len(ss)):
            if ss!= s[0:len(ss)]:
                ss=str(ss)+str(s[0])
                s=s[1:]
            else:
                l=len(ss)
                flag=False
                if len(s)%l !=0:
                    pass
                else:
                    for i in range(0,len(s),l):
                        if ss == s[i:i+l]:
                            flag=True
                        else:
                            flag=False
                            break
                if(flag):
                    return True
                ss=str(ss)+str(s[0])
                s=s[1:]
        if s==ss:
            return True
        return False
        