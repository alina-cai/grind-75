from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        window = SortedList()

        for i, n in enumerate(nums):
            window.add(n)

            if len(window) > k:
                window.remove(nums[i - k])

            if i >= k - 1:
                res.append(min(0, window[x - 1]))

        return res