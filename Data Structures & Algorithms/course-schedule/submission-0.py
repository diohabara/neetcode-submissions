from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for nc in graph[course]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0:
                    q.append(nc)
        return taken == numCourses