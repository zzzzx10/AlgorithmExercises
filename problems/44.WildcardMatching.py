class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s) + 1
        len_p = len(p) + 1
        dp = [[False] * len_s for _ in range(len_p)]
        s = "#%s" % s
        p = "#%s" % p
        dp[0][0] = True
        for row in range(1, len_p):
            if p[row] == "*":
                dp[row][0] = dp[row - 1][0]

            for col in range(1, len_s):
                if s[col] == p[row] or p[row] == "?":
                    dp[row][col] = dp[row - 1][col - 1]
                elif p[row] == "*":
                    dp[row][col] = dp[row][col - 1] or dp[row - 1][col]
                else:
                    dp[row][col] = False
        #print(dp)
        return dp[len_p - 1][len_s - 1]


solution = Solution()
s = "abc"
p = "a*"
print(solution.isMatch(s, p))
p = "??"
print(solution.isMatch(s, p))
p = "?*"
print(solution.isMatch(s, p))
