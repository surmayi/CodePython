def findInsertPosition(nums,target):
    low=0
    high= len(nums)-1
    mid=0
    if high==0:
        return 0
    while low<high:
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    if target>nums[low]:
        return low+1
    return low

nums=[1,3,5,6]
target=2
print(findInsertPosition(nums,target))
