class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if not prereqs[course]:
                return True

            visited.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereqs[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# O(n*p), O(n)