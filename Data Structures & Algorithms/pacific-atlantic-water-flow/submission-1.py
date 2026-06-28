class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        

        def dfs(i, j, sea):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                return
            
            # Check if already visited
            if sea == "p" and (i, j) in pacific:
                return
            if sea == "a" and (i, j) in atlantic:
                return
            
            # Add current cell to the sea
            if sea == "p":
                pacific.add((i, j))
            else:
                atlantic.add((i, j))
            
            
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < len(heights) and 0 <= new_j < len(heights[0]) and heights[i+direction[0]][j+direction[1]] >= heights[i][j]:
                    dfs(i+direction[0], j+direction[1], sea)
            return
        
        for i in range(len(heights[0])):
            dfs(0, i, "p")
        for i in range(len(heights)):
            dfs(i, 0, "p")
        for i in range(len(heights[0])):
            dfs(len(heights)-1, i, "a")
        for i in range(len(heights)):
            dfs(i, len(heights[0])-1, "a")
        
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        return result
        