class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numrows, numcols = len(board), len(board[0])

        def comb(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= numrows or c >= numcols or word[i] != board[r][c] or board[r][c] == '#':
                return False
            
            
            #this means that we visitied this cell
            board[r][c] = '#'

            res = comb(r + 1, c, i + 1) or comb(r - 1, c, i + 1) or comb(r, c + 1, i + 1) or comb(r, c - 1, i + 1)
            
            board[r][c] = word[i]

            return res

        for i in range(numrows):
            for j in range(numcols):
                if comb(i, j, 0):
                    return True
        return False

            
        