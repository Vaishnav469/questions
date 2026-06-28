class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        visited = set()
    
        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for edges in hashmap[curr]:
                dfs(edges)
            return

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res