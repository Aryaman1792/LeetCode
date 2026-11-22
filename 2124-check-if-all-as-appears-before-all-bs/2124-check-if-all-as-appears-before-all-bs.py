class Solution:
    def checkString(self, s: str) -> bool:
        flag=True
        for i in s:
            if i=='a' and flag==False:
                return False
            elif i=='a' and flag==True:
                continue
            else:
                flag=False
        return True

        