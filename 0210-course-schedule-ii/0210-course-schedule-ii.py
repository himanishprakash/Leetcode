class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

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

        answer = []

        while queue:
            node = queue.popleft()
            answer.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(answer) == numCourses:
            return answer
        else:
            return []
        