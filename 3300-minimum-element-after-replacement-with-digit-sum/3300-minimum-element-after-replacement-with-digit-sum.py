class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            c=0
            for j in str(nums[i]):
                c+=int(j)
            lst.append(c)
        return min(lst)
                
        