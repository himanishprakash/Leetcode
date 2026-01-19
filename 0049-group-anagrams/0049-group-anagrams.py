class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        diction = defaultdict(list)

        for i in strs:
            s = ''.join(sorted(i))
            diction[s].append(i)

        return list(diction.values())