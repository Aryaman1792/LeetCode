class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        a=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                a+=1
        return a
        