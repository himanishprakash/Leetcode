class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        lat = 0
        lon = 0
        answer = 0

        for i in range(len(s)):

            if s[i] == 'N':
                lat += 1
            elif s[i] == 'S':
                lat -= 1
            elif s[i] == 'W':
                lon -= 1
            elif s[i] == 'E':
                lon += 1

            answer = max(answer, min(abs(lat) + abs(lon) + k* 2, i +1) )
        
        return answer