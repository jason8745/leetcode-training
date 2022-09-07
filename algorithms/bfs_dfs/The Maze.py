#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
1.用了visit(set)紀錄走訪過的節點
2.dfs搭配stack結構,做到backtrack往回退一步重新決策的效果
3.directions的操作,每到新的點都有四個方向可以嘗試
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m,n = len(maze),len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        stack = [start]
        while stack:
            curx,cury = stack.pop()
            if [curx,cury]==destination:
                return True
            for dirx,diry in directions:
                # 每走到新的點,都可能有四個方向可以走
                tx,ty = curx,cury
                while 0<= tx+dirx <m and 0<=ty+diry <n and not maze[tx+dirx][ty+diry]:
                    # 確認沒有碰到邊界才走
                    tx,ty = tx+dirx,ty+diry
                if (tx,ty) not in visit:
                    # 沒走過就加進visit,走過了就不走
                    visit.add((tx,ty))
                    stack.append((tx,ty))
        return False