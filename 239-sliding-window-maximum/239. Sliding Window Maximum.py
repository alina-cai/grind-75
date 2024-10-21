class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
            
        deq = deque()
        res = []
        l, r = 0, 0

        while r < len(nums):
            while deq and deq[-1] < nums[r]:
                deq.pop()

            deq.append(nums[r])

            if r - l + 1 == k:
                res.append(deq[0])

                if deq[0] == nums[l]:
                    deq.popleft()

                l += 1

            r += 1

        return res

# O(n), O(k)