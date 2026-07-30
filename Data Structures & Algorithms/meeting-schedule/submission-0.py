"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
    
        ans=[Interval(intervals[0].start,intervals[0].end)]
        for interval in intervals[1:]:
            if interval.start<ans[-1].end:
                ans[-1].end=max(ans[-1].end,interval.end)
            else:
                ans.append(Interval(interval.start,interval.end))
        if len(ans)==len(intervals):
            return True
        else:
            return False