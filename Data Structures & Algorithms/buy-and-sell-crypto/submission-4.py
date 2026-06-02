class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                if j<len(prices) and prices[j]<prices[i]:
                    break
                elif j<len(prices) and prices[j]>prices[i]:
                    maxres=prices[j]-prices[i]
                    res=max(maxres,res)
        return res
        