class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        

        if not points:
            return 0


        answer = 1

        points.sort(key = lambda x: x[1] )
        first_arrow = points[0][1]

        for x, y in points:

            if first_arrow < x:
                answer += 1
                first_arrow = y

        return answer
             