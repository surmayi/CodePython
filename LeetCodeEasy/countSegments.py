class Solution(object):
    def countSegments(self, s):
        count=0
        s=s.strip()
        if len(s)>0 and s[0]!=' ':
            count=1
        l =len(s)
        i=0
        while(l>0 and ' ' in s):
            if s[i]==' ':
                while(l>0 and s[i]==' '):
                    i+=1
                    l-=1
                count+=1
            i+=1
            l-=1
        return count