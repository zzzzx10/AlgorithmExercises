class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        i = 0
        while i < l / 2:
            sub = s[:i + 1]
            split = s.split(sub)
            if len(split) <= 2 or "".join(split):
                i += 1
            else:
                return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        # 假设母串S是由子串s重复N次而成， 则 S+S则有子串s重复2N次，
        # 现在S=Ns， S+S=2Ns 因此S在(S+S)[1:-1]中必出现一次以上
        return (s + s)[1:-1].find(s) != -1
        # return (s + s).find(s, 1) != len(s)


s = "a"
solution = Solution()
print(solution.repeatedSubstringPattern(s))
