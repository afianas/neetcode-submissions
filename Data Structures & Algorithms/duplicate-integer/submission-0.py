class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=0
        for i in range(0,len(nums)):
         for j in range(i+1,len(nums)):
          if nums[i]==nums[j]:
           flag=flag+1
        if flag==0:
          return False
        return True