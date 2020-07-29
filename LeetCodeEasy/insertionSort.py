def insertionSort(nums):
    for i in range(1,len(nums)):
        cur= nums[i]
        for j in range(i-1,-1,-1):
            if cur < nums[j]:
                nums[j+1],nums[j] = nums[j],cur
            else:
                nums[j+1] = cur
                break
    return nums