class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = []
        graph = [[] for _ in range(numCourses)]
        numPrereqs = [0] * numCourses

        #all courses with their prereqs
        for c,p in prerequisites:
            graph[p].append(c)
            numPrereqs[c] += 1
        q = []
        for c, n in enumerate(numPrereqs):
            if n == 0:
                q.append(c)
        while q:
            course = q.pop(0)
            taken.append(course)
            for c in graph[course]:
                numPrereqs[c] -= 1
                if numPrereqs[c] == 0:
                    q.append(c)

        return True if len(taken) == numCourses else False 





        
        
        
        

        return False
    
        