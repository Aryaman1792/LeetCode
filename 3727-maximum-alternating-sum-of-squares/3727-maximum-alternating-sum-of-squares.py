class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[]
        for i in range(len(nums)):
            num.append(abs(nums[i]))
        num.sort()
        num.reverse()
        a=0
        if len(num)%2==0:
            for i in range(len(num)/2):
                a+=num[i]*num[i]
            for j in range(len(num)-1,len(num)/2-1,-1):
                a-=num[j]*num[j]
        else:
            for i in range(len(num)/2+1):
                a+=num[i]*num[i]
            for j in range(len(num)-1,len(num)//2,-1):
                a-=num[j]*num[j]
        return a
