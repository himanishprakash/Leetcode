class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        left = 0
        stored = set()
        max_width = 0

        for i in range(len(s)):

            while s[i] in stored:
                stored.remove(s[left])
                left += 1

            stored.add(s[i])

            max_width = max(max_width, i - left + 1)

        return max_width


