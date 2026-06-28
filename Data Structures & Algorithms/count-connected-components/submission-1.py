class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        visited = set()
    
        def dfs(curr, prev):
            if curr in visited:
                return
            visited.add(curr)
            for edges in hashmap[curr]:
                if prev is not None and edges==prev:
                    continue
                dfs(edges, curr)
            return
        res = 1
        dfs(0, None)
        for i in range(1, n):
            if visited and i not in visited:
                dfs(i, None)
                res += 1
        return res