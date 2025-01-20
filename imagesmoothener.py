class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0]*n for _ in range(m)]
        directions = [(-1,-1),(-1,1),(-1,0),(0,0),(0,-1),(1,-1),(1,0),(0,1),(1,1)]
        for i in range(m):
            for j in range(n):
                count = 0
                total = 0
                for dy,dx in directions:
                    x,y = i+dx,j+dy
                    if 0<=x<m and 0<=y<n:
                        total+=img[x][y]
                        count+=1
                res[i][j] = total//count
        return res
