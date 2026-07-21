class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        intervals.append(newInterval)

        intervals.sort()

        result = []

        for i in intervals:

            if not result or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result
