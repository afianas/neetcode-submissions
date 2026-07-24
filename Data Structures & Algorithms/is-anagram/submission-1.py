class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1
        for t in t:
            freq[ord(t)-ord('a')]-=1

        for n in freq:
            if n==0:
                continue
            else:
                return False
        return True