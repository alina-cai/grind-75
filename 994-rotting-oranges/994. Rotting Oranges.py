class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for nr, nc in directions:
                    newR, newC = nr + r, nc + c

                    if (
                        newR in range(ROWS) and
                        newC in range(COLS) and
                        grid[newR][newC] == 1
                    ):
                        q.append((newR, newC))
                        grid[newR][newC] = 2
                        fresh -= 1

            res += 1

        return res if fresh == 0 else -1