def findIntersection(arr1,arr2):
    i=0
    j=0
    s=set()
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            s.add(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return s


A = [2, 3, 3, 5, 7, 11]
B = [3, 5, 7, 15, 31]

print(findIntersection(A, B))