class Solution:
    def trap(self, height):

        water = [0] * len(height)
        pre = height[0]
        if len(height) <= 2:
            return 0
        for i, e in enumerate(height):
            if i == 0:
                continue
            if e < pre:
                water[i] = pre - e
            else:
                pre = e
        # print(water)
        last = height[-1]
        for i, e in enumerate(height[::-1]):
            if i == 0:
                water[-1] = 0
            if e < last:
                water[-i - 1] = min(last - e, water[-i - 1])
            else:
                water[-i - 1] = 0
                last = e
            # print(i,e,water)
        # print(water)
        return sum(water)


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution.trap(height))
height = [2, 0, 2]
print(solution.trap(height))
