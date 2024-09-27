class Solution:
    def longestPalindrome(self, s: str) -> int:
        countS = Counter(s)
        odd = 0

        for ch, count in countS.items():
            if count % 2 == 1:
                odd += 1

        if odd:
            return len(s) - odd + 1

        return len(s)