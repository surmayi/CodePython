def rotate( nums, k):
        while(k>0):
            nums.insert(0,nums.pop())
            k-=1
        return nums

rotate([-1,-100,3,99],2)