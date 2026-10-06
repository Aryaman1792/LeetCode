class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=b=0
        for ch in s:
            if ch=="(":
                a+=1
            elif a:
                a-=1
            else:
                b+=1
        return a+b
        