class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            res.append(nums.copy())

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
                res.append(p)

            nums.append(n)

        return res

# O(n!n), O(n)