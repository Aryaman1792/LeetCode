class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum>9*num:
            return ""
        a=[]
        for i in range(num):
            m=min(9,sum)
            a.append(str(m))
            sum-=m
        return "".join(a)
        