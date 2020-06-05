def getRow(self, rowIndex):
        k=rowIndex
        final=[]
        if rowIndex>=1:
            final.append([1])
        else:
            return [1]
        row=1
        while(row<=rowIndex):
            temp=[1]
            for i in range(1,row):
                temp.append(final[-1][i-1]+final[-1][i])

            temp.append(1)
            final.append(temp)
            row+=1
        return (final[-1])

getRow(3)