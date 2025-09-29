class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        

        courses.sort(key = lambda x: x[1])

        total_duration = 0
        max_heap = []

        for duration, deadline in courses:

            total_duration += duration
            heapq.heappush(max_heap, -duration)
            
            if total_duration > deadline:

                longest = -heapq.heappop(max_heap)
                total_duration -=  longest


        return len(max_heap)

