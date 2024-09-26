class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, cur = 0, float('inf')

        for p in prices:
            cur = min(cur, p)
            res = max(res, p - cur)

        return res