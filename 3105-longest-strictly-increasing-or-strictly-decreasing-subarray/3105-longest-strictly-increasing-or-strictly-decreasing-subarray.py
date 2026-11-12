class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a=1
        b=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                a+=1
                b=max(b,a)
            else:
                a=1
        c=1
        d=1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
                d=max(c,d)
            else:
                c=1
        return max(b,d)

            
        