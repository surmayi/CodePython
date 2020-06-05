def longestCommonPrefix( strs):
        pre = set()
        i=0
        if(len(strs)<=1):
            return ''.join(strs)
        first = strs[0]
        strs.pop(0)
        for i in range(len(first)):
            flag=True
            for st in strs:
                if((len(st)<=i) or (st[:i+1]!=first[:i+1])):
                    flag =False
                    break
            if(flag==False):
                return first[:i]
        return first[:i+1]

longestCommonPrefix(["flower","flow","flight"])


