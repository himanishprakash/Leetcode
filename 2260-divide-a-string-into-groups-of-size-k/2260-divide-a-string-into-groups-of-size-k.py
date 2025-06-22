class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        answer = ""
        result = []
        for i in s:
            answer += i
            
            if len(answer) == k:
                result.append(answer)
                answer = ""

        if answer == "":
            return result
        
        elif len(answer) != k:
            while len(answer)  != k:
                answer += fill

            result.append(answer)

        return result


