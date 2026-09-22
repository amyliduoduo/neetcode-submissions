class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #initialize grid dimensions and visited hashsets
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        #dfs helper method - reverse flow
        def dfs(r, c, visit, prevHeight):
            #base case stop recursion
            if ((r, c) in visit or #already visited
                r < 0 or c < 0 or
                r == ROWS or c == COLS or #out of bounds
                heights[r][c] < prevHeight #current cell is lower than the previous cell
            ):
                return
            
            visit.add((r, c)) #the target set tracking
            #Recursively calls dfs on all four adjacent neighbors (Down, Up, Right, Left) 
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            #launching DFS from top&bottom borders
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            #launching DFS from left&right borders
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        #Loops through every cell (r, c), If both pac and atl sets, added to res list
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res



