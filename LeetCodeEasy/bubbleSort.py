def bubbleSort(nums):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
    return nums 