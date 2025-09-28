class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        indegree = [0] * numCourses
        adj = []

        for _ in range(numCourses):
            adj.append([])

        for prereq in prerequisites:

            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        
        
        queue = deque()

        for i in range(numCourses):

            if indegree[i] == 0:
                queue.append(i)

        nodes_visited = 0

        while queue:
            node = queue.popleft()
            nodes_visited += 1

            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return nodes_visited == numCourses




