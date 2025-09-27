class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])

        answer = 0

        staring = float('-inf')

        for x, y in intervals:

            if x >=  staring:
                staring = y

            else:
                answer += 1

            
        return answer