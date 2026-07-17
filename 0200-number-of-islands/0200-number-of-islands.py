class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visted=[]
        for  i in range(row):
            visted.append([0]*col)

        count=0
        for i  in range(row):
            for j in range(col):
                if grid[i][j]=="1" and visted[i][j]==0:
                    self.bfs(grid,visted,i,j)
                    count+=1
        return count
    def bfs(self,grid,visted,i,j):
        row=len(grid)
        col=len(grid[0])
        q=deque()
        q.append((i,j))
        visted[i][j]=1
        while q:
            i,j=q.popleft()
            
            if i-1>=0 and grid[i-1][j]=="1" and visted[i-1][j]==0:
                q.append((i-1,j))
                visted[i-1][j]=1
            if j+1<col and grid[i][j+1]=="1" and visted [i][j+1]==0: 
                q.append((i,j+1))
                visted[i][j+1]=1
            if i+1<row and grid[i+1][j]=="1" and visted[i+1][j]==0:
                q.append((i+1,j))
                visted[i+1][j]=1
            if j-1>=0 and grid[i][j-1]=="1" and visted[i][j-1]==0:
                q.append((i,j-1))
                visted[i][j-1]=1          


