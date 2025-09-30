class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        max_day = 0
        n = len(events)
        
        for i in events:
            max_day = max(max_day, i[1])

        events.sort()
        max_heap = []
        answer =  j = 0

        for i in range(1, max_day + 1):

            while j < n and events[j][0] <= i:
                heappush(max_heap,events[j][1] )
                j += 1

            while max_heap and max_heap[0] < i:
                heappop(max_heap)

            if max_heap:
                heappop(max_heap)
                answer += 1


        return answer



            



        


        