class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #only horizontally and vertically is an island
        #BFS

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0]) #len(grid[0]): Accesses the first row (grid[0]) and counts its elements to get the total number of columns
        visit = set() #hashset for visited elements
        islands = 0 #count of islands

        def bfs(r,c):
            #Put the starting cell (r, c) into a queue
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            #While the queue is not empty, pop the front cell
            while q:
                row, col = q.popleft()#popleft means pop the first element we added
                #check all directions: up, down, left, right
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    #check the boundary of the neighbor cell
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visit):
                        
                        q.append((nr, nc))
                        visit.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit: #if visit 1
                   bfs(r, c) #dfs defined below
                   islands += 1
        return islands







