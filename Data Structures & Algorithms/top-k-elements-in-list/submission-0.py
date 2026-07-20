from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums1={}
        for num in nums:
            nums1[num]=nums1.get(num,0)+1
        freq=[0]*(len(nums)+1)
        for i in range(len(freq)):
            freq[i]=[]
        for num,c in nums1.items():
            freq[c].append(num) #freq[c]=num will lead to overwriting
        l=0
        ans=[]
        for i in range(len(freq)-1,0,-1):
            if freq[i]==[]:
                continue
            else:
                for num in freq[i]:
                    l+=1
                    ans.append(num)
                    

                if l==k:
                    return ans
