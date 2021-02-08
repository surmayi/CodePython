def searchForRange(nums,target):
    low=0
    high= len(nums)-1
    mid=0
    rang=[]
    while low<=high:
        mid= (low+high)//2
        print(mid)
        if target==nums[mid]:
            if target!=nums[mid-1]:
                break
            high=mid-1
        elif target<nums[mid]:
            high =mid-1
        else:
            low=mid+1
    print(mid)
    if target!=nums[mid]:
        return [-1,-1]
    rang.append(mid)
    print(nums[mid])
    while mid<len(nums) and nums[mid]==target:
        mid += 1
    rang.append(mid-1)
    return rang


nums=[1]
target=1
print(searchForRange(nums,target))