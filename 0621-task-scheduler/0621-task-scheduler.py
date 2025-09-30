class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task = [0] * 26

        for t in tasks:
            task[ord(t) - ord('A')] += 1

        task.sort()

        max_slot = task[25] - 1
        idle_slot = max_slot * n

        for i in range(24, -1, -1):
            idle_slot -= min(max_slot,task[i] )

        if idle_slot > 0:
            return idle_slot + len(tasks)

        else:
            return len(tasks)