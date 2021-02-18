def getPeakElement(nums):
    low=0
    high=len(nums)-1
    if high in [0,1]:
        return nums.index(max(nums))
    while low<=high:
        mid =(low+high)//2
        if mid>0 and mid<len(nums)-1:
            print(nums[mid],nums[mid-1],nums[mid+1])
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                print('Found')
                return mid
            elif nums[mid]>nums[mid-1]:
                low=mid+1
            else:
                high=mid-1
        else:
            return mid

nums=[1,2,3,4,5]
print(getPeakElement(nums))