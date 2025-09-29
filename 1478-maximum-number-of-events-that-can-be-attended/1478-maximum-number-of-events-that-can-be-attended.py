class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        n = len(events)
        max_day = 0

        for i in events:
            max_day = max(max_day, i[1])

        events.sort()
        array = []
        answer = j = 0

        for i in range(1,max_day + 1):

            while j < n and events[j][0] <= i:
                heapq.heappush(array,events[j][1] )
                j +=1
                

            while array and array[0] < i:
                heapq.heappop(array)

            if array:
                heapq.heappop(array)
                answer += 1

        return answer

        