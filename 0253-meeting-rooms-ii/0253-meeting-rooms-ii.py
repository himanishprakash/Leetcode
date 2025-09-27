class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])

        answer = []

        heapq.heappush(answer, intervals[0][1])

        for i in intervals[1:]:

            if answer[0] <= i[0]:
                heapq.heappop(answer)


            heapq.heappush(answer,i[1])

        return len(answer)




