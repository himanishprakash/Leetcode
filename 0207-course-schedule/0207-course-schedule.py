class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        indegree = [0] * numCourses

        adj = []

        for _ in range(numCourses): 
            adj.append([])

        for a,b in prerequisites: 
            adj[b].append(a)
            indegree[a] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)


        nodes_visited = 0

        while queue: 
            node = queue.popleft()
            nodes_visited += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)

        return nodes_visited == numCourses 


        

        