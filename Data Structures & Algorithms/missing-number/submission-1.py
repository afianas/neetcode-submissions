class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        result=0
        for num in nums:
            res^=num
        for i in range(0,len(nums)+1):
            result^=i
        return res^result
            
        