class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = [False] * n

        def dfs(node):

            for neigbour in adj[node]:
                if visit[neigbour]:
                    continue
                else:
                    visit[neigbour] = True
                    dfs(neigbour)
        
        res = 0
        for r in range(n):
            if visit[r]:
                continue;
            else:
                visit[r] = True
                dfs(r)
                res += 1

        return res
