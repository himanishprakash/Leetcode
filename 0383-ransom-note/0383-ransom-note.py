class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        if len(ransomNote) > len(magazine):
            return False

        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)

        for key, value in counter_r.items():
            
            if value > counter_m[key]:
                return False


        return True