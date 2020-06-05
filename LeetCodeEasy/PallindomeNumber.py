def isPalindrome( x):
        n=0
        temp =x
        while(x>0):
            n = n*10 + x%10
            x =int(x)/10
        if n==temp:
            return True
        return False
isPalindrome(10)
isPalindrome(101)