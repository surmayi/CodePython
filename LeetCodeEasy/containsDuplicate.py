def containsDuplicate( nums):
        ol= len(nums)
        nl= len(set(nums))
        if ol==nl:
            return False
        return True


containsDuplicate([1,2,3,1])
containsDuplicate([1,2,3,4])