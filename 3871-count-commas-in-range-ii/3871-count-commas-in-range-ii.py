class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1000
        c=1
        while b<=n:
            nv=b*1000-1
            if nv>n:
                nv=n
            a+=(nv-b+1)*c
            b*=1000
            c+=1
        return a
        