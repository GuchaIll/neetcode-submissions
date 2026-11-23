class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(x,y):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if grid[x][y] == "0":
                return

            grid[x][y] = "0"

            for dx,dy in neighbors:
                nx = dx + x
                ny = dy + y

                dfs(nx,ny)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        
        return islands
            
        

            