class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=""
        res=""
        count=0
        for i in range(0,len(s)):
            l,r=i,i
            while(l>=0) and r<len(s) and s[l]==s[r]:
                ans=s[l:r+1]
                count+=1
                l-=1
                r+=1
        for i in range(0,len(s)):
            l,r=i,i+1
            while(l>=0) and r<len(s) and s[l]==s[r]:
                ans=s[l:r+1]
                count+=1
                l-=1
                r+=1
        return count