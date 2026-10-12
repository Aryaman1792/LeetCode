class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a,b,c=0,1,1
        while c<=n:
            if a+b+c==n:
                return True
            a=b
            b=c
            c=a+b
        return a+b+c==n
        