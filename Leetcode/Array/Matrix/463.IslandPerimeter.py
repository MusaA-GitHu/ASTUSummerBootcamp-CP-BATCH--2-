#Solved by ma

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        su=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    su+=4
                    if j>0 and grid[i][j-1]==1:
                        su-=2
                    if i>0 and grid[i-1][j]==1:
                        su-=2
              #su+=grid[I][j]
        return su
            
