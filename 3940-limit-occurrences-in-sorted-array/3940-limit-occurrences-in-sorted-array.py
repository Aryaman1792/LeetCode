class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c=Counter(nums)
        lst=[]
        for i in c:
            if c[i]>k:
                for j in range(k):
                    lst.append(i)
            else:
                e=c[i]
                for j in range(e):
                    lst.append(i)
        return lst
        # lst=[]
        # lst.append(nums[0])
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
                