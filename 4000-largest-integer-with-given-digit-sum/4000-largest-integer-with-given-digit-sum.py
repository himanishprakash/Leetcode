class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        

        if 9 * n < s:
            return -1 

        if s ==0:
            return 0

        result = []
        for _ in range(n):

            minimum = min(9,s)
            result.append(str(minimum))

            s -= minimum
        return int(''.join(result))