class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses

        adj = []

        for _ in range(numCourses):
            adj.append([])

        for a, b in prerequisites:

            adj[b].append(a)
            indegree[a] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodevisited = 0

        while queue:
            node = queue.popleft()
            nodevisited += 1

            for neighbour in adj[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)


        return nodevisited == numCourses