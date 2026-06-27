class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = []
        for i in range(n):
            adj.append([])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        def dfs(node, par):
            if node in cycle:
                return False
            
            cycle.add(node)
            for neigbour in adj[node]:
                if neigbour == par:
                    continue
                else:
                    if not dfs(neigbour, node):
                        return False
            return True
        
        return dfs(0, -1) and len(cycle) == n
            
        