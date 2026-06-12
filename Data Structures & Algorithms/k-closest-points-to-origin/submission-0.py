import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        r=[]
        for x,y in points:
            dist=x**2+y**2
            res.append([dist,x,y])
        heapq.heapify(res)
        for i in range(0,k):
            r.append(heapq.heappop(res)[1:])

        return r
