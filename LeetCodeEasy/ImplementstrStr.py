def strStr( haystack, needle):
        if(needle not in haystack):
            return -1
        return haystack.index(needle)

strStr('hello','ll')
strStr('hello','lol')