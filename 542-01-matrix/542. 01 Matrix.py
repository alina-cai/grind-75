class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))

        res = 0
        visited = set()

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if (
                    r not in range(ROWS) or
                    c not in range(COLS) or
                    (r, c) in visited
                ):
                    continue

                mat[r][c] = res
                visited.add((r, c))

                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))

            res += 1

        return mat