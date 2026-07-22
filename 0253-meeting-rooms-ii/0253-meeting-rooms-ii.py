class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end= []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()

        starts, ends = 0, 0
        result, count = 0, 0

        while starts < len(intervals):

            if ends >= len(end) or start[starts] < end[ends]:

                starts += 1
                count += 1

            else:
                count -= 1
                ends += 1

            result = max(result,count)


        return result