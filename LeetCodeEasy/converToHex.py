class Solution(object):
    def toHex(self, num):
        val=''
        if(num==0):
            return str(0)
        if(num<0):
            num=num+ 2**32
        while(num>0):
            d=num%16
            if d==10:
                val='a'+val
            elif d==11:
                val='b'+val
            elif d==12:
                val='c'+val
            elif d==13:
                val='d'+val
            elif d==14:
                val='e'+val
            elif d==15:
                val='f'+val
            else:
                val=str(d)+val
            num=num//16
        return val
        