def isIsomorphic(self, s, t):
        if(len(s)!=len(t)):
            return False
        if(len(s)==1):
            return True
        dicS ={}
        dicT ={}
        for i in range(len(s)):
            if(s[i] in dicS.keys()):
                if(dicS[s[i]]!=t[i]):
                    return False
            else:
                dicS[s[i]]=t[i]
                if(t[i] in dicT.keys()):
                    if(dicT[t[i]]!=s[i]):
                        return False
                else:
                    dicT[t[i]]=s[i]
        return True

isIsomorphic('ab','aa')
isIsomorphic('egg','add')