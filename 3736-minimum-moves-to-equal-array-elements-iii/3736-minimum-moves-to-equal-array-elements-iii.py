class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        z=nums[-1]
        a=0
        for i in range(len(nums)-1):
            b=z-nums[i]
            a+=b
        return a
        