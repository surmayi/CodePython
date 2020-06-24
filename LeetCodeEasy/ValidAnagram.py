def isAnagram( s, t):
        if(len(s)!=len(t)):
            return False
        dic= {}
        for ch in s:
            if ch in dic.keys():
                dic[ch]+=1
            else:
                dic[ch] =1
        for ch in t:
            if ch in dic.keys():
                dic[ch]-=1
            else:
                return False
        for val in dic.values():
            if(val!=0):
                return False
        return True