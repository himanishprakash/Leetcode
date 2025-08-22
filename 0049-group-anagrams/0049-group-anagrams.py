class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicts = defaultdict(list)

        for i in strs:

            string = ''.join(sorted(i))

            dicts[string].append(i)


        return list(dicts.values())