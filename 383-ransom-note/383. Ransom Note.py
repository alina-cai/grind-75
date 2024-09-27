class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countA, countB = Counter(ransomNote), Counter(magazine)

        for ch, count in countA.items():
            if ch not in countB or countB[ch] < count:
                return False

        return True