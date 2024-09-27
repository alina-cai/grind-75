class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        c1, c2 = 2, 3

        for i in range(4, n + 1):
            dp = c1 + c2
            c1 = c2
            c2 = dp

        return c2