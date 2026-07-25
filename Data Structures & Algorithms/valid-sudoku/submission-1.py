class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create three hash maps of hashsets
        #Passing set to defaultdict tells Python that whenever a key doesn't exist yet, it should automatically create an empty Python set
        cols = defaultdict(set)
        rows = defaultdict(set) #rows is a map where each key is a row index (0 to 8) and each value is a set() of numbers already seen in that row.
        squares = defaultdict(set)
        
        #loop through each cell
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True