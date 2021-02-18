def findMinElementInCyclicArray(nums):
    low=0
    high=len(nums)-1
    while low<=high:
        mid= (low+high)//2
        if mid>0 and mid<len(nums)-1:
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            elif nums[mid]>nums[mid-1]:
                high=mid-1
            else:
                low=mid+1
        else:
            return mid


nums=[4,5,6,1,2,3]
print(findMinElementInCyclicArray(nums))