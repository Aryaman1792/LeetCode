class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        c=nums[0]
        a=nums[-1]
        b=nums[-2]
        return a+b-c
        