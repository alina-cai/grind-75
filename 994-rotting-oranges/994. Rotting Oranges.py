class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def rot(r, c):
            nonlocal fresh 
            
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        res = 0

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)

            res += 1

        return res if fresh == 0 else -1

# O(m*n), O(m*n)