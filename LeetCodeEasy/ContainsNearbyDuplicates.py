from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        defdic = defaultdict(int)
        for ind, d in enumerate(nums):
            if d in defdic and ind - defdic[d]<= k:
                return True
            defdic[d] = ind
        return False