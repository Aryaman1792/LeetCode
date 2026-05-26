class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d=0
        for i in s:
            for j in t:
                if i==j:
                    d+=abs(s.index(i)-t.index(j))
        return d

        