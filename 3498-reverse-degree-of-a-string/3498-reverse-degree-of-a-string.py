class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        mul=1
        a=0
        for i in range(len(s)):
            x=123-ord(s[i])
            a+=x*mul
            mul+=1
        return a
            


            
        