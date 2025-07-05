class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counts = Counter(arr)
        answer = -1
        
        for key , value in counts.items():

            if key == value:
                answer = max(answer,key)


        return answer