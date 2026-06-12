
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        for i in range(0,k):
            res=heapq.heappop(nums)
        return -res                                                                                                                                                                                                  