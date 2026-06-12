import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        for i in range(n):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        res=[0]*n
        print(stones)
        i=1
        while len(stones)>1:
            s1=-heapq.heappop(stones)
            s2=-heapq.heappop(stones)
            print(s1)
            print(s2)
            if s1!=s2:
                heapq.heappush(stones,-(s1-s2)) #insert negative
        if not stones:
            return 0
        return -stones[0]          #return negative
