class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for ch in s:
            if ch in bmap:
                if not stack or stack.pop() != bmap[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack