class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        count = collections.Counter(magazine)

        for r in ransomNote:
            if count[r] <= 0:
                return False

            count[r] -= 1

        return True

# time: O(n)
# space: O(1)