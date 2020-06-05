def merge( nums1, m, nums2, n):
        if(nums1 is None) and nums2 is None:
            return None
        else:
            if nums1 is None:
                nums1=nums2
                return nums1
            else:
                if nums2 is None:
                    return nums1
        i=1
        j=0
        while(i<=n):
            nums1.pop()
            i+=1
        i=0
        while(i<m) and (j<n):
            if(nums1[i]<nums2[j]):
                i+=1
            else:
                nums1.insert(i,nums2[j])
                j+=1
                m+=1
                i+=1
            
        while(j<n):
            
            nums1.insert(i,nums2[j])
            j+=1
            i+=1
        return nums1

nums1 = [-1,-1,0,0,0,0]
nums2 = [-1,0]
print(merge(nums1,4,nums2,2))