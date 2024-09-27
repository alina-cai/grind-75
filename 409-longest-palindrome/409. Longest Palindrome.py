class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        odd = 0

        for ch in s:
            dic[ch] = 1 + dic.get(ch, 0)

            if dic[ch] % 2 == 1:
                odd += 1
            else:
                odd -= 1

        if odd > 0:
            return len(s) - odd + 1

        return len(s)
