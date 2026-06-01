class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
        # lst=[]
        # for i in range(len(nums)):
        #     if nums[i] in lst:
        #         return True
        #     lst.append(nums[i])
        # return False        