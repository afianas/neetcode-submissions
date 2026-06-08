class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        
        l1=0
        l2=r-1
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        while(l1<=l2):
            m=(l1+l2)//2
            if nums[m]<target:
                l1=m+1
            elif nums[m]>target:
                l2=m-1
            else:
                return m
        return -1
            