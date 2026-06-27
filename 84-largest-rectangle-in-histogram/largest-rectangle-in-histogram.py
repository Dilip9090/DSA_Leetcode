class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):

            currHeight = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > currHeight:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea