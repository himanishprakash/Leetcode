class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        

        counts.sort()

        max_slot = counts[25] - 1
        idle_slots = max_slot * n

        for i in range(24, -1, -1):
            idle_slots -= min(max_slot, counts[i])

        if idle_slots >0:
            return idle_slots + len(tasks)
        else:
            return len(tasks)
        