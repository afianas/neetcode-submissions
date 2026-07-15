class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        ans=[intervals[0]]
        for start,end in intervals[1:]:
            if start<ans[-1][1]:
                count+=1
                if end<ans[-1][1]:
                    ans[-1]=[start,end]
            else:
                ans.append([start,end])
        return count