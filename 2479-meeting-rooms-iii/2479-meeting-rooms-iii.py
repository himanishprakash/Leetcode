class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        room_avail_time = [0] * n
        meeting_counts = [0] * n

        for start, end in sorted(meetings):
            min_room_avail_time = inf
            room_index = 0
            room_found = False

            for i in range(n):
                if room_avail_time[i] <= start: 
                    room_found = True   
                    meeting_counts[i] += 1
                    room_avail_time[i] = end
                    break

                if min_room_avail_time > room_avail_time[i]:
                    min_room_avail_time = room_avail_time[i]
                    room_index = i
            
            if not room_found:
                room_avail_time[room_index] += end - start
                meeting_counts[room_index] += 1


        return meeting_counts.index(max(meeting_counts))