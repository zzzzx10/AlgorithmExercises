class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['1', 0]]
        for x in s:
            if stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([x, 1])

        return "".join([c * k for c, k in stack])


solution = Solution()
s = "deeedbbcccbdaa"
k = 3
print(solution.removeDuplicates(s, k))
s = "pbbcggttciiippooaais"
k = 2
print(solution.removeDuplicates(s, k))
s = "abcd"
k = 2
print(solution.removeDuplicates(s, k))
