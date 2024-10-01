class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            dist = sqrt(x ** 2 + y **2)
            distances.append((dist, x, y))

        distances.sort()

        res = []

        for i in range(k):
            _, x, y = distances[i]
            res.append([x, y])

        return res