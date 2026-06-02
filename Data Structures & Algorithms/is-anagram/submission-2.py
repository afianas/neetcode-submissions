class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one=[]
        two=[]
        for i in range(0,len(s)):
         one.append(s[i])
        for j in range(0,len(t)):
         two.append(t[j])  
        if sorted(one)==sorted(two):
         return True
        else:
         return False