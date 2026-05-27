class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        r=[0]*(amount+1)
        r[0]=1
        for c in coins:
            for a in range(c,amount+1):
                r[a]+=r[a-c]
        return r[amount]