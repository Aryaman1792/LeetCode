class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]==0:
                a+=1
        for j in range(len(nums)-1,-1,-1):
            if nums[j]!=0 and a>0:
                b+=1
                a-=1
            elif nums[j]==0:
                a-=1
        return b