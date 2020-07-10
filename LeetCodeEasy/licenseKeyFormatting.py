class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = ''.join(S.split('-')).upper()
        l = len(S)//K
        t= S[0:len(S)%K]
        S=S[len(S)%K:]
        i=1
        d=0
        while(l>0):
            d=d + K*i
            S=S[0:d]+'-'+ S[d:]
            d=i
            l-=1
            i+=1
        if len(t)==0:
            return S[:len(S)-1]
        if len(S)==0:
            return t
        return t+'-'+S[:len(S)-1]
        