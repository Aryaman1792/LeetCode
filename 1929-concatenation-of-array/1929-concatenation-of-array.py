class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            lst.append(nums[i])
        for j in range(len(nums)):
            lst.append(nums[j])
        return lst
        