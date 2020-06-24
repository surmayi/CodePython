def getHint(secret, guess):
        B=0
        C=0
        l=len(secret)
        i=0
        while(i<l):
            if(guess[i]==secret[i]):
                B+=1
                secret=secret[:i]+secret[i+1:]
                guess =guess[:i]+guess[i+1:]
                l-=1
                i-=1
            i+=1
        for i,ch in enumerate(secret):
            if ch in guess:
                C+=1
                secret=secret.replace(ch,'',1)
                guess =guess.replace(ch,'',1)
        return str(B)+'A'+str(C)+'B'