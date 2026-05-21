class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix=set()
        for i in arr1:
            x=i
            while x>0:
                prefix.add(x)
                x//=10 
        ans=0
        for num in arr2:
            x=num
            while x>0:
                if x in prefix:
                    ans=max(ans,len(str(x)))
                x//=10
        return ans
            
                