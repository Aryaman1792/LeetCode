class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        a=Counter(n)
        b=0
        for i in a:
            b+=int(i)*int(a[i])
        return b
            
        