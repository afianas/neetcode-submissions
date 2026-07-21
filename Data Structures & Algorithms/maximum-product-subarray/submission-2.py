class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        ans=-float("inf")
        for i in range(len(nums)):
            suffix*=nums[i]
            ans=max(suffix,ans)

            if suffix==0:
                suffix=1
        for i in range(len(nums)-1,-1,-1):
            prefix*=nums[i]
            ans=max(prefix,ans)

            if prefix==0:
                prefix=1

        return ans        