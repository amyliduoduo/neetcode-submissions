class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS, go through each [r][c] to find 1 and "sink" it, check neighbors - recursively visits and changes
        
        #initialize directions, grid dimensions, island counter
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        #dfs helper method
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0"): #if it's 0 or out of bounds
                return #stops the recursion
            else:
                grid[r][c] = "0" #"sink" the land cell

            for dr, dc in directions: #explore neighbors
                dfs(r + dr, c + dc)

        #main loop to check the cell and call dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

