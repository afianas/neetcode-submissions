class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        finres=0
        r=1
        while r<len(prices):
            if prices[l]>prices[r] and r<len(prices):
                l=r
                r+=1
            else:
                res=prices[r]-prices[l]
                finres=max(res,finres)
                r+=1
        return finres

                

        