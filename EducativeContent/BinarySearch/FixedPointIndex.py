def fixedPointIndex(nums):
    low=0
    high=len(nums)-1
    match=[-1]
    while low<=high:
        mid= (low+high)//2
        if nums[mid]==mid:
            match.append(mid)
            high=mid-1
        elif nums[mid]>mid:
            high=mid-1
        else:
            low=mid+1
    return match[-1]


nums=[0,2,5,8,17]
print(fixedPointIndex(nums))