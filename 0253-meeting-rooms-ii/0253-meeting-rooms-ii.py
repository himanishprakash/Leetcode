class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        array = []
        heappush(array,intervals[0][1] )
        for i in intervals[1:]:

            if array[0] <= i[0]:
                heappop(array)      
            
            heappush(array,i[1])  

        return len(array)