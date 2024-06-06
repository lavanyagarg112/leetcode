class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        p1 = 0
        p2 = len(height) - 1

        ans = min(height[p2],height[p1])

        while p1 < p2:

            width = p2 - p1
            length = min(height[p1], height[p2]) 
            ans = max(ans, width * length)

            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        return ans