class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res=None
        for i, ele in enumerate(nums):
            if i!=ele:
                if res is None:
                    res=ele
                else:
                    res &= ele
        if res==None:
            return 0
        return res
        