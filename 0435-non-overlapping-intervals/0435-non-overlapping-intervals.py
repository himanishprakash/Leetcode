class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        answer = 0
        removed = float("-inf")

        for x, y in intervals:

            if x >= removed:
                removed = y

            else:
                answer += 1

        return answer
        