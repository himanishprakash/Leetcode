class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        start = []
        end = []

        for i in intervals:

            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()
        s, e = 0 , 0
        count, result  = 0, 0


        while s < len(intervals):

            if e >= len(end) or start[s] < end[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -=1 

            result = max(result, count)


        return result
        