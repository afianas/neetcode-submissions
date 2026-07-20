class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        nums=heights
        maxi=0
        while l<r:
            water=min(nums[l],nums[r])*(r-l)
            maxi=max(maxi,water)
            if nums[l]<=nums[r]:
                l+=1
            else:
                r-=1
        return maxi