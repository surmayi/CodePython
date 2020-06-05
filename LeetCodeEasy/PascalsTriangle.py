def generate( numRows):
        k=numRows
        final=[]
        if numRows>=1:
            final.append([1])
        row=1
        while(row<numRows):
            temp=[1]
            for i in range(1,row):
                temp.append(final[-1][i-1]+final[-1][i])

            temp.append(1)
            final.append(temp)
            row+=1
        return (final)

generate(5)