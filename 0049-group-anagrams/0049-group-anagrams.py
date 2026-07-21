class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = defaultdict(list)

        for i in strs:
            sorted_ans = ''.join(sorted(i))

            result[sorted_ans].append(i)


        return list(result.values())

