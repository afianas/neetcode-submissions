class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1
        for q in t:
            freq[ord(q)-ord('a')]-=1
        
        for x in freq:
            if x==0:
                continue
            else:
                return False
        return True