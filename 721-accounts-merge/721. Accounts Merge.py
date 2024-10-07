class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = {}

        for i, a in enumerate(accounts):
            for j in range(1, len(a)):
                if a[j] not in emailMap:
                    emailMap[a[j]] = []

                emailMap[a[j]].append(i)

        visited = [False] * len(accounts)

        def dfs(i, emails):
            if visited[i]:
                return

            visited[i] = True

            for j in range(1, len(accounts[i])):
                emails.add(accounts[i][j])
                for e in emailMap[accounts[i][j]]:
                    dfs(e, emails)

        res = []

        for i, a in enumerate(accounts):
            if visited[i]:
                continue

            name, emails = a[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))

        return res