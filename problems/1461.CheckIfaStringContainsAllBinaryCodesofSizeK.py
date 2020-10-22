class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        length = len(s)
        if length < 2 ** k:
            return False
        subset = set()
        for i in range(0, length-k+1):
            subset.add(s[i:i+k])
        if len(subset) == 2 ** k:
            return True
        else:
            return False
        # def getsub(k):
        #     sublist = ["0", "1"]
        #     for _ in range(k - 1):
        #         sublist, temp = [], sublist
        #         for i in temp:
        #             sublist.append(i + "0")
        #             sublist.append(i + "1")
        #     return sublist
        #
        # sub = getsub(k)
        # for item in sub:
        #     if s.find(item) < 0:
        #         return False
        # return True


solution = Solution()
s = "0000000001011100"
k = 4
print(solution.hasAllCodes(s, k))
s = "00110110"
k = 2
print(solution.hasAllCodes(s, k))
s = "00110"
k = 2
print(solution.hasAllCodes(s, k))
