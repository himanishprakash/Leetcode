class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        

        points.sort(key = lambda x: x[1])

        answer = 1
        arrow = points[0][1]

        for arr_str, arr_end in points:

            if arr_str > arrow:
                answer += 1
                arrow = arr_end

        return answer
