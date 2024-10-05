class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        res = [intervals[0]]

        for i in range(len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])

        return res

# O(n), O(n)