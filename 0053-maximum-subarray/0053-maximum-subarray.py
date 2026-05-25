class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=nums[0]
        b=nums[0]
        for num in nums[1:]:
            b=max(num,b+num)
            a=max(a,b)
        return a
        