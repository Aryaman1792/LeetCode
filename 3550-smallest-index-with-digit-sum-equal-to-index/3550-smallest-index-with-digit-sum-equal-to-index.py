class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            a=0
            for j in str(nums[i]):
                a+=int(j)
            if a==i:
                return i
        return -1

        