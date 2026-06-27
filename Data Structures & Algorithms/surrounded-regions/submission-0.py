class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numrows, numcols = len(board), len(board[0])

        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= numrows or c >= numcols or board[r][c] == '#' or board[r][c] == 'X':
                return
            
            
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(numrows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][numcols - 1] == "O":
                dfs(r, numcols - 1)

        for c in range(numcols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[numrows - 1][c] == "O":
                dfs(numrows - 1, c)
            
            
        
        for r in range(numrows):
            for c in range(numcols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
       
                
               
        