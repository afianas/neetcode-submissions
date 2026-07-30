class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        q=deque()

        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0

        
        def addOrange(r,c):
            if (r<0 or r==rows or c<0 or c==cols or (r,c) in visit or grid[r][c]==0 or grid[r][c]==2):
                return
            q.append((r,c))
            visit.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2
                addOrange(r+1,c)
                addOrange(r-1,c)
                addOrange(r,c+1)
                addOrange(r,c-1)
            dist+=1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return dist-1