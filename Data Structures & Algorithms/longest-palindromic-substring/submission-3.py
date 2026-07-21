class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        res=""
        resLen=0
        for i in range(0,len(s)):
            l,r=i,i
            while(l>=0) and r<len(s) and s[l]==s[r]:
                ans=s[l:r+1]
                if len(ans)>resLen:
                    res=ans
                    resLen=max(resLen,len(ans))
                l-=1
                r+=1
        for i in range(0,len(s)):
            l,r=i,i+1
            while(l>=0) and r<len(s) and s[l]==s[r]:
                ans=s[l:r+1]
                if len(ans)>resLen:
                    res=ans
                    resLen=max(resLen,len(ans))
                l-=1
                r+=1
        return res
