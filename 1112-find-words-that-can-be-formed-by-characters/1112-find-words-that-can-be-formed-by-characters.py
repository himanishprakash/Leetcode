class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        counts = [0] * 26

        for c in chars:
            counts[ord(c) - ord("a")] += 1

        
        answer = 0

        for word in words:

            count = [0] * 26

            for w in word:
                count[ord(w) - ord('a')] += 1

            good = True

            for i in range(26):
                if counts[i] < count[i]:
                    good = False
                    break

            if good:
                answer += len(word)

        return answer

            
        
