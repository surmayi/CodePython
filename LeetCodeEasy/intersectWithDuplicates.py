class Solution(object):
    def intersect(self, nums1, nums2):
        li=[]
        for val in nums1:
            if val in nums2:
                li.append(val)
                nums2.remove(val)
        return li