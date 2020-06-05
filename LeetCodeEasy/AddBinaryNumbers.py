def addBinary(a, b):
        aval=0
        bval=0
        for i in range(len(a)):
            aval = aval+(2**(len(a)-i-1))*int(a[i])
        for i in range(len(b)):
            bval = bval+(2**(len(b)-i-1))*int(b[i])
        total = aval+bval
        return str(bin(total)[2:])

addBinary('101','11')