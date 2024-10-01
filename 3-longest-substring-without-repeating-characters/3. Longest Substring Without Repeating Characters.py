class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        visited = set()
        l = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])

            res = max(res, r - l + 1)

        return res

# O(n), O(n)