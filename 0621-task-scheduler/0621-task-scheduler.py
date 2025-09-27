class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1


        freq.sort()

        max_freq = freq[25] - 1

        idle_slot = max_freq * n
        
        for i in range(24, -1 , -1):

            idle_slot -= min(freq[i],max_freq)
     
        
        if idle_slot > 0:
            return idle_slot + len(tasks)
        else:
            return len(tasks)

