class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #graph for course with its prereqs
        graph = [[] for _ in range(numCourses)]
        numPrereqs = [0] * numCourses
        taken = []
        for c, p in prerequisites:
            graph[p].append(c)
            numPrereqs[c] += 1
        q = []
        for i, n in enumerate(numPrereqs):
            if n == 0:
                q.append(i)

        while q:
            course = q.pop(0)
            taken.append(course)

            for c in graph[course]:
                numPrereqs[c] -= 1
                if numPrereqs[c] == 0:
                    q.append(c)
        

        return taken if len(taken) == numCourses else []
        