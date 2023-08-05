'''
Leetcode- https://leetcode.com/problems/number-of-islands/
'''

'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        noRows = len(grid)
        noCols = len(grid[0])
        for row in range(noRows):
            for col in range(noCols):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    island+=1
        return island

    def dfs(self,grid,row,col):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]=="0":
                return

            grid[row][col] = "0"

            self.dfs(grid,row-1,col)
            self.dfs(grid,row+1,col)
            self.dfs(grid,row,col-1)
            self.dfs(grid,row,col+1)

# T:  O(M * N), where M is the number of rows in the grid and N is the number of columns.

'''
Explanation:

1.Initialize island to 0.
2.Calculate noRows (number of rows) and noCols (number of columns) of the grid.
3.Start looping through each cell in the grid using nested loops.
4.For each cell, if the cell contains "1", call the dfs function to explore the island.
5.Inside the dfs function, check if the current cell is out of bounds or if it's water ("0"). If either condition is met, return from the function.
6.Mark the current cell as visited by changing its value to "0".
7.Recursively call dfs on the neighboring cells (up, down, left, right).
8.Repeat steps 5-7 until all connected land cells are visited and marked as "0". This essentially explores and marks an entire island.
9.Go back to the main function, increment the island count by 1.
R10.epeat steps 4-9 for all cells in the grid.


Now, let's dry run the code step by step using the provided input grid:

1.Initialize island to 0.
2.Calculate noRows = 4 and noCols = 5.

Start looping through each cell in the grid:

- Cell at (0, 0) contains "1":

    - Call dfs at (0, 0).
        -- Mark (0, 0) as "0".
        -- Call dfs at (0, -1), which returns immediately.
        -- Call dfs at (0, 1), which recursively calls dfs on (0, 2) and (1, 1), both return immediately.
        -- Call dfs at (-1, 0), which returns immediately.
        -- Call dfs at (1, 0), which recursively calls dfs on (2, 0), which calls dfs on (2, 1), (3, 0), and (1, 0), all return immediately.
        -- Call dfs at (0, 0) again (through recursion), which returns immediately.
    - Increment island to 1.

- Cell at (0, 1) contains "1":

    - Call dfs at (0, 1), which returns immediately.
- Continue this process for all cells in the grid.

Final island count: 3
'''