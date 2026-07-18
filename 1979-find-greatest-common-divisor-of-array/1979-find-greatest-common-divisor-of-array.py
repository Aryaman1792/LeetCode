class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[0]
        b=nums[-1]
        for i in range(a,0,-1):
            if b%i==0 and a%i==0:
                return i
        return 1

        