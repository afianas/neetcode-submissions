from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1=defaultdict(list)
        

        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            strs1[tuple(count)].append(word)
        return list(strs1.values())