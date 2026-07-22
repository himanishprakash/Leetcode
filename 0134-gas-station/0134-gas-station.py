class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return  -1

        current_gas = 0
        start = 0
        for i in range(len(gas)):

            if gas[i] - cost[i] > 0:
                current_gas += gas[i] - cost[i]

            else:
                current_gas = 0
                start = i + 1


        return start