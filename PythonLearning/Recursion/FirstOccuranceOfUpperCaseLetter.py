def findFirstUpperCase(st,ind=0):
    if st[ind].isupper():
        return st[ind]
    if len(st)-1==ind:
        return 'No upper case letter'
    return findFirstUpperCase(st,ind+1)


print(findFirstUpperCase('linearAlgebra'))