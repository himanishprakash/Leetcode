class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        stack = []

        for i in intervals:

            if not stack or i[0] > stack[-1][1]:
                stack.append(i)


            else:
                stack[-1][1] = max(stack[-1][1], i[1])
                

        return stack