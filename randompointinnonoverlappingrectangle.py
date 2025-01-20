class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        self.total_area = 0
        for rect in rects:
            area = (rect[2]-rect[0]+1) * (rect[3]-rect[1]+1)
            self.total_area +=area
            self.areas.append(self.total_area)
        

    def pick(self) -> List[int]:
        r = random.randint(1,self.total_area)
        for i in range(len(self.rects)):
            if r<=self.areas[i]:
                rect = self.rects[i]
                x = random.randint(rect[0],rect[2])
                y = random.randint(rect[1],rect[3])
                return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
