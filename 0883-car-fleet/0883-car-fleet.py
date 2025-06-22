class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        stack = []

        combined = sorted(zip(position, speed), reverse = True)

        print(combined)

        for p, s in combined:

            reach = (target - p) / s

            stack.append(reach)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        


        return len(stack)