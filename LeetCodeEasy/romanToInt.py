def romanToInt(self, s):
        symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        letters = list(s)
        num+=symbols[letters[0]]
        letters.pop(0)
        for i,ch in enumerate(letters):
            if(i==0):
                if(symbols[ch]>num):
                    num = symbols[ch]-num
                else:
                    num+=symbols[ch]
            else:
                if(symbols[ch]>symbols[letters[i-1]]):
                    num = num - 2*symbols[letters[i-1]] + symbols[ch]
                else:
                    num+=symbols[ch]
        return num

romanToInt('III')
romanToInt('LVIII')
romanToInt('MCMXCIV')