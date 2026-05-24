class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]%=k
        mini=float('inf')
        # count=0
        for x in range(k):
            for y in range(k):
                if x==y:
                    continue
                count=0

                for i in range(n):
                    if i%2==0:
                        diff=abs(nums[i]-x)
                        count+=min(diff,k-diff)
                    else:
                        diff=abs(nums[i]-y)
                        count+=min(diff,k-diff)
                mini=min(count,mini)
        return mini
        