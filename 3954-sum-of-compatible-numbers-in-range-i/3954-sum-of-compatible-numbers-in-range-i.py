class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        b=n+k+1
        a=n-k
        a=max(0,a)
        c=0
        for i in range(a,b):
            if (n&i)==0:
                c+=i
        return c
        