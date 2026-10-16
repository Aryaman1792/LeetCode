class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a={}
        for i in s:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        b={}
        for i in t:
            if i not in b:
                b[i]=1
            else:
                b[i]+=1
        return a==b
        

        