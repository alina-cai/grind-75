class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            s1, e1 = res[-1]
            s2, e2 = intervals[i]

            if s2 > e1:
                res.append(intervals[i])
            else:
                res[-1] = [min(s1, s2), max(e1, e2)]

        return res