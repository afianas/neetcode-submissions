class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        ans=-float("inf")
        for i in range(len(nums)):
            

            if suffix==0:
                suffix=1
            suffix*=nums[i]
            ans=max(suffix,ans)
        for i in range(len(nums)-1,-1,-1):
            if prefix==0:
                prefix=1
            prefix*=nums[i]
            ans=max(prefix,ans)

            

        return ans        