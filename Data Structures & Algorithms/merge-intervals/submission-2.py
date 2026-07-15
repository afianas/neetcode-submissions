class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=intervals[0]
        i=0
        resu=[]
        while i<len(intervals):
            while i<len(intervals)-1 and res[1]>=intervals[i+1][0]:
                res=[min(res[0],intervals[i+1][0]),max(res[1],intervals[i+1][1])]
                i+=1
            resu.append(res)
            i+=1
            if i<len(intervals):
                res=intervals[i]
        return resu


