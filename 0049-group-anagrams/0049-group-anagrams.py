class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = defaultdict(list)

        for i in strs:

            sudo  =''.join(sorted(i))

            result[sudo].append(i)

        return list(result.values())