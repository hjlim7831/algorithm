class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        intervals.sort(key=lambda x: (x[0], x[1]))

        tmp = intervals[0]
        for start, end in intervals[1:]:
            if tmp[0] != start and tmp[1] <= start:
                tmp = [start, end]
                continue
            
            answer += 1
        
        return answer
            
