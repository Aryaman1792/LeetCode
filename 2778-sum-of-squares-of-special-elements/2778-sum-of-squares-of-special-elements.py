class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        a=0
        for i in range(1,len(nums)+1):
            if n%i==0:
                b=i-1
                a+=nums[b]*nums[b]
        return a

        