class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for edges in hashmap[curr]:
                if prev is not None and edges==prev:
                    continue
                if not dfs(edges, curr):
                    return False
            return True
        return dfs(0, None) and len(visited) == n
            