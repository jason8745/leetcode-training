#############
# Author : Yujun Wen
# Last edit: 2022/9/6
# email: yujunwen0517@gmail.com
#####
"""
Note
dfs的重點是要找到停止的點,跟下一步,以及visited
"""
# DFS解法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        count = 0
        cols,rows = len(grid),len(grid[0])
        for i in range(cols):
            for j in range(rows):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count
    
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i >= len(grid) or j>= len(grid[0]) or grid[i][j]!='1':
            return
        
        grid[i][j]='@'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
# time complexity O(MN)
# Space complexity O(MN)

# BFS解法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        count = 0
        cols,rows = len(grid),len(grid[0])
        for i in range(cols):
            for j in range(rows):
                if grid[i][j]=='1':
                    count+=1
                    self.bfs(grid,i,j)
        return count
    
    
    def bfs(self,grid,i,j):
        queue = deque([(i,j)])
        grid[i][j] = '@'
        while queue:
            i,j = queue.popleft()
            for delta_i,delta_j in [(-1,0),(1,0),(0,-1),(0,1)]:
                next_i = i+delta_i
                next_j = j+delta_j
                if next_i<0 or next_j<0 or next_i>=len(grid) or next_j >= len(grid[0]) or grid[next_i][next_j]!='1':
                    continue
                queue.append((next_i,next_j))
                grid[next_i][next_j]='@'
                
# time complexity O(MN)
# Space complexity O(min(M,N))