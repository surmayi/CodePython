class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        for id,val in enumerate(nums1):
            idx = nums2.index(val)
            flag = False
            while(idx<len(nums2)-1):
                if nums2[idx+1]>val:
                    nums1[id] = nums2[idx+1]
                    flag =True
                    break;
                else:
                    idx+=1
            if not flag:
                nums1[id] = -1
        return nums1
        