class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        r=0
        for i in range(len(nums)):
            st=set()
            for j in range(i,n):
                st.add(nums[j])
                m=len(st)
                r+=m*m
        return r

        