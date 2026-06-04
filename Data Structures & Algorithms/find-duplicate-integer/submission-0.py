class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check=set()
        for num in nums:
            if num not in check:
                check.add(num)
            else:
                return num
        