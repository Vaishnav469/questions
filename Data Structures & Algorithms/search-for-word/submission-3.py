class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def backtrack(i, j, curr):
            if curr == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] == word[curr]:
                tmp = board[i][j]
                board[i][j] = "#"
                for direction in directions:
                    if backtrack(i + direction[0], j + direction[1], curr+1):
                        return True
                board[i][j] = tmp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
