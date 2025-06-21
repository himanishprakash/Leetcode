class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        counts = Counter(word)
        result = len(word)
        for i in counts.values():
            deleted = 0
            for b in counts.values():
                if i >b:
                    deleted += b

                elif b > i + k:
                    deleted += b -(i + k)

            result = min(result, deleted)

        return result
            