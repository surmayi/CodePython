def selectionSort(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]<nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
    return nums