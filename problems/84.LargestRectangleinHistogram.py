class Solution:
    def largestRectangleArea(self, heights) -> int:
        length = len(heights)
        maxsq = 0
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        for i in range(1, length + 2):
            # 高度为heights[stack[-1]]的矩形可以确定了,最后再append i
            while (heights[i] < heights[stack[-1]]):
                print("pop", stack, heights[stack[-1]], heights[stack[-2]])
                a = stack.pop()
                maxsq = max(maxsq, heights[a] * (i - stack[-1] - 1))
                print(stack, maxsq)
            stack.append(i)
            print("append", stack)

        return maxsq


solution = Solution()
height = [2, 1, 5, 6, 2, 3]
print(solution.largestRectangleArea(height))
height = [1, 3, 2, 3, 4, 2, 1]
print(solution.largestRectangleArea(height))
height = [2, 2]
print(solution.largestRectangleArea(height))
