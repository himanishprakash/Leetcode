class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        results = defaultdict(list)

        for i in strs: 
            
            answer = ''.join(sorted(i))

            results[answer].append(i)


        return list(results.values())