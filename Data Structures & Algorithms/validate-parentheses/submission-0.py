class Solution:
    

    def isValid(self, s: str) -> bool:
        hashmap={'(':')','{':'}','[':']'}
        stack=[]
        for i in range(len(s)):
            if s[i] in hashmap:
                stack.append(s[i])
            else:
                if not stack or hashmap[stack.pop()]!=s[i]:
                    return False
                else:
                    continue
        return False if stack else True
                



        