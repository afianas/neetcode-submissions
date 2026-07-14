import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0,len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if (x==y):
                continue
            elif x<y:
                x=-x
                y=-y
                heapq.heappush(stones,y-x)
        return -stones[0] if stones else 0
