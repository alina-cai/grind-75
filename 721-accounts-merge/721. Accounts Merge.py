class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailsMap = {}

        for i, a in enumerate(accounts):
            for j in range(1, len(a)):
                if a[j] not in emailsMap:
                    emailsMap[a[j]] = []

                emailsMap[a[j]].append(i)

        res = []

        def dfs(i, emails):
            if visited[i]:
                return

            visited[i] = True

            for j in range(1, len(accounts[i])):
                emails.add(accounts[i][j])
                
                for e in emailsMap[accounts[i][j]]:
                    dfs(e, emails)

        visited = [False] * len(accounts)

        for i, a in enumerate(accounts):
            if visited[i]:
                continue

            name, emails = a[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))

        return res