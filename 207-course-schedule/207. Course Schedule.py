class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:
            prereqs[c].append(p)

        visited = set()

        def dfs(c):
            if c in visited:
                return False

            visited.add(c)

            for p in prereqs[c]:
                if not dfs(p):
                    return False

            visited.remove(c)
            prereqs[c] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# O(m+n), O(m+n)