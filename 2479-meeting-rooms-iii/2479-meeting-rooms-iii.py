class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        room_avail_time = [0] * n
        meeting_count = [0] * n

        for start, end in sorted(meetings):

            min_available_time_room = inf
            min_avail_time = 0
            find_unused_room =False

            for i in range(n):

                if room_avail_time[i] <= start:
                    find_unused_room =True
                    room_avail_time[i] = end
                    meeting_count[i] += 1
                    break

                if min_available_time_room > room_avail_time[i]:
                    min_available_time_room = room_avail_time[i]
                    min_avail_time = i

            if not find_unused_room:
                room_avail_time[min_avail_time] += end -start
                meeting_count[min_avail_time] += 1

        
        return meeting_count.index(max(meeting_count))







        