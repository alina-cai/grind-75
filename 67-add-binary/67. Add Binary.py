class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        res = ""
        a, b = a.zfill(n), b.zfill(n)
        carry = 0

        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1

            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                res += "1"
            else:
                res += "0"

            carry //= 2

        if carry:
            res += "1"
            
        return res[::-1]