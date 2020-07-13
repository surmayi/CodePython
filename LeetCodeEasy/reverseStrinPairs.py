class Solution(object):
    def reverseStr(self, s, k):
        l = len(s)
        arr=[]
        for i in range(0,l,k):
            arr.append(s[i:i+k])
        for i in range(len(arr)):
            if i%2==0:
                arr[i]=arr[i][::-1]
        return ''.join(arr)
        