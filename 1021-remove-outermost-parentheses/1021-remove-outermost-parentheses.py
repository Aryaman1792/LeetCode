class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        b=0
        for c in s:
            if c=="(":
                if b>0:
                    a+=c
                b+=1
            else:
                b-=1
                if b>0:
                    a+=c
        return a
        