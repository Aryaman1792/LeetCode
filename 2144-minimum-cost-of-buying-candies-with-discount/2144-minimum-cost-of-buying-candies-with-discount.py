class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        a=0
        c=0
        for i in range(len(cost)-1,-1,-1):
            if c==2:
                c=0
                continue
            else:
                c+=1
                a+=cost[i]
        return a


        