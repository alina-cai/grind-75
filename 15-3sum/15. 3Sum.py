class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if n > 0:
                break

            l, r = i + 1, len(nums) - 1

            while l < r:
                cur = nums[l] + nums[r] + n

                if cur == 0:
                    res.append([nums[l], nums[r], n])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif cur > 0:
                    r -= 1
                else:
                    l += 1

        return res