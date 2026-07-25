class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countp={}
        counts={}
        if len(s1)>len(s2):
            return False
        elif s1=="":
            return True

        for ch in s1:
            countp[ch]=countp.get(ch,0)+1
        for i in range(len(s1)):
            counts[s2[i]]=counts.get(s2[i],0)+1

        if countp==counts:
            return True
        
        l=0
        for r in range(len(s1),len(s2)):
            counts[s2[r]]=counts.get(s2[r],0)+1
            counts[s2[l]]-=1
            if counts[s2[l]]==0:
                del counts[s2[l]]
            l+=1
            print(counts)
            print(countp)
            if counts==countp:
                return True
        return False