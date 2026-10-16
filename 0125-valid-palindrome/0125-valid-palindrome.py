class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]
        for i in s:

            if i.isalpha():
                a.append(i.lower())
            elif i.isdigit():
                a.append(i)

        if a==a[::-1]:
            return True
        return False