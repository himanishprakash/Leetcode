class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        n = len(events)
        max_day = 0
        for event in events:
            max_day = max(max_day, event[1])

        events.sort()
        arr = []

        ans = j =0

        for i in range(1, max_day + 1):

            while j < n and events[j][0] <= i:
                heapq.heappush(arr, events[j][1])
                j += 1

            while arr and arr[0] < i:
                heapq.heappop(arr)

            if arr:
                heapq.heappop(arr)
                ans += 1

        return ans

        
        
