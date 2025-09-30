class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key = lambda x:x[1])

        total_time = 0
        result = []

        for duration, deadline in courses:

            total_time += duration
            heappush(result, -duration)
            if total_time > deadline:
                longest = -heappop(result)
                total_time -= longest

        return len(result)


            
        
