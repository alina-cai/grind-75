class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())

                return

            for n in nums:
                if n not in cur:
                    cur.append(n)
                    dfs(cur)
                    cur.pop()

        dfs([])

        return res