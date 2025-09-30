class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        target = newInterval[0]

        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid -1 

        intervals.insert(left,newInterval)

        
        result = []


        for i in intervals:

            if not result or result[-1][1] < i[0]:
                result.append(i)

            else:
                result[-1][1] = max(result[-1][1], i[1])


        return result
        