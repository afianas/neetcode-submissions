class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        maxi=0
        if len(s)==1:
            return s
        for i in range(0,len(s)):
            for j in range(1,len(s)):
                strs=s[i:j+1]
                if strs==strs[::-1]:
                    if len(strs)>maxi:
                        ans=strs
                        maxi=max(maxi,len(strs))
        return ans