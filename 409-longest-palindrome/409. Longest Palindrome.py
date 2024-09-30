class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        odd = 0

        for ch in s:
            count[ch] = 1 + count.get(ch, 0)

            if count[ch] % 2 == 1:
                odd += 1
            else:
                odd -= 1

        if odd:
            return len(s) - odd + 1
        
        return len(s)