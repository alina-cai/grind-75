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

                for x, y in directions:
                    nr, nc = x + r, y + c

                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2

            res += 1

        return res if fresh == 0 else -1