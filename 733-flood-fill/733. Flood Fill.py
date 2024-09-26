class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return

            if r not in range(ROWS) or c not in range(COLS):
                return

            if image[r][c] != originalColor:
                return

            visited.add((r, c))
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return

        originalColor = image[sr][sc]
        dfs(sr, sc)

        return image


# 0 1 0
# 0 0 1