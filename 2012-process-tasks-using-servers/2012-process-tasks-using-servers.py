class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        n = len(servers)
        ans, busy_server = [], []

        free_servers = list(zip(servers,range(n)))
        heapify(free_servers)

        for time, task in enumerate(tasks):
            
            while busy_server and busy_server[0][0] <= time:
                sec, weight, idx = busy_server[0]

                if sec != time:
                    break
                heappush(free_servers, (weight, idx))
                heappop(busy_server)

            
            if free_servers == []:
                sec, weight, idx = heappop(busy_server)
                heappush(busy_server, (sec + task, weight, idx))

            else:
                weight, idx = heappop(free_servers)
                heappush(busy_server, (time + task, weight, idx))
                
            ans.append(idx)

        return ans
