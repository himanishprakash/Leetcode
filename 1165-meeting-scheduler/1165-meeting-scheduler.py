class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        left = right = 0
        slots1.sort()
        slots2.sort()

        while left < len(slots1) and right < len(slots2):

            meetingstart = max(slots1[left][0],slots2[right][0] )
            meetingend = min(slots1[left][1],slots2[right][1] )

            if meetingend - meetingstart >= duration:
                return [meetingstart,meetingstart + duration]

            if slots1[left][1] < slots2[right][1]:
                left += 1
            else:
                right += 1


        return []
