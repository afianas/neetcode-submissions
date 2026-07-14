
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest=[]
        for i in range(len(nums)):
            n=nums[i]
            heapq.heappush(largest,n)

            if len(largest)>k:
                heapq.heappop(largest)

        return heapq.heappop(largest)                                                                                                                                                                                