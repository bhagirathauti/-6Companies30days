class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        xClosest = max(x1,min(xCenter,x2))
        yClosest = max(y1,min(y2,yCenter))
        distance = sqrt((xClosest-xCenter)**2+(yClosest-yCenter)**2)
        return distance<=radius

        
