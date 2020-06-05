def isPalindrome( s):
        normal =[]
        for i in range(len(s)):
            if s[i].isalnum():
                normal.append(s[i].lower())
        l = len(normal)
        flag=True
        for i in range(int(l/2)):
            if(normal[i]==normal[l-i-1]):
                flag=True
            else:
                flag = False
                break
        return flag

isPalindrome('0P')
isPalindrome('A man, a plan, a canal: Panama')