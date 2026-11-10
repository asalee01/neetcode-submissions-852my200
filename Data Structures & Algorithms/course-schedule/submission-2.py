class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Kahn's algorithm uses heap and indegree

        #create an adjacency list
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        visited = set()

        for pre, curr in prerequisites:
            graph[pre].append(curr)
            degree[curr] += 1
        q = deque()

        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            visited.add(course)
            for c in graph[course]:
                degree[c] -= 1
                if degree[c] == 0:
                    q.append(c)
        

        return True if len(visited) == numCourses else False
