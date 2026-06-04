class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=0
        r=1
        result=[0]*len(temperatures)
        print(result)
        while(l<len(temperatures)):
            if l<len(temperatures) and r<len(temperatures) and temperatures[l]<temperatures[r]:
                result[l]=r-l
                l+=1
                r=l+1
            elif r>len(temperatures):
                result[l]=0
                l+=1
                r=l+1
            else:
                r+=1
            if l==len(temperatures)-1:
                result[l]=0
        return result
            