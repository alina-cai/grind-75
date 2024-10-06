class TimeMap:

    def __init__(self):
        self.storage = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.storage.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            v, t = values[m]

            if t <= timestamp:
                res = v
                l = m + 1
            else:
                r = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)