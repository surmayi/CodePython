def wordPattern(pattern, str):
        dic={}
        li = str.split()
        if(len(pattern)!=len(li)):
            return False
        for i,ch in enumerate(pattern):
            if ch in dic.keys():
                if(dic[ch]!=li[i]):
                    return False
            else:
                if(li[i] in dic.values()):
                    return False
                dic[ch]=li[i]
        return True