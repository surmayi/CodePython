def lengthOfLastWord( s):
        if len(s)==0:
            return 0
        st = s.split()
        if len(st)==0:
            return 0
        return len(st[-1])

lengthOfLastWord('Hello World')