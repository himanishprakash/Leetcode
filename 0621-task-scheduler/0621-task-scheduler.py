class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        element = [0] * 26

        for task in tasks:

            element[ord(task) - ord('A')] += 1

        element.sort()

        max_Slot = element[25] - 1

        idle_slot = max_Slot * n

        for i in range(24,-1,-1):
            idle_slot -= min(max_Slot, element[i])

        
        if idle_slot > 0:
            return idle_slot + len(tasks)

        else:
            return len(tasks)

        