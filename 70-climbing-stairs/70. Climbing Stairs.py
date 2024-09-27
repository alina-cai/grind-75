class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        n1, n2 = 2, 3

        for n in range(4, n + 1):
            dp = n1 + n2
            n1 = n2
            n2 = dp

        return n2

# O(n), O(1)