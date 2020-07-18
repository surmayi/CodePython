class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        from statistics import mean 
        if len(nums)<k:
            return 0
        if len(nums)==k:
            return mean(nums)
        avg1 =0

        for i in range(0,len(nums)):
            if len(nums[i:i+k])==k and sum(nums[i:i+k])>avg1*k:
                avg1 = mean(nums[i:i+k])
        return avg1




#Using numpy(efficient -)

sums = np.cumsum([0] + nums)
print(sums)
return int(max(sums[k:] - sums[:-k])) / k