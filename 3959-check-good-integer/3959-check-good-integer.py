class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        a=0
        b=0
        for i in str(n):
            a+=int(i)
            b+=int(i)**2
        return b-a>=50
