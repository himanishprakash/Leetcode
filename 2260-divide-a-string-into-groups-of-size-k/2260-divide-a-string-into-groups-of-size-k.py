class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        result = []

        n = len(s)
        current = 0
        while current < n :
            result.append(s[current: current + k])
            current += k


        result[-1] += fill * (k - len(result[-1]))

        return result


        
       




