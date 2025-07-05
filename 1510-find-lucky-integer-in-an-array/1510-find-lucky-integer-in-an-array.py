class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counts = Counter(arr)
        answer = -1
        count = dict(sorted(counts.items()))
        
        for key , value in count.items():

            if key == value:
                answer = key


        return answer