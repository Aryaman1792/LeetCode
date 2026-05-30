class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        ans=0
        for i in range(n):
            sm=0
            for j in range(i,n):
                sm+=nums[j]
                seen.add(nums[j])
                ans+=sm in seen 
            seen.clear()
        return ans
        