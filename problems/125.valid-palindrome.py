class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isok(ch):
            if ch.isalpha() or ch.isdigit():
                return True
            else:
                return False

        s = [x for x in s if isok(x)]
        length = len(s)
        flag = True
        for i in range(length // 2):
            front = s[i]
            end = s[length - 1 - i]
            if front.isdigit() and end.isdigit() and front == end:
                continue
            elif end.isalpha() and front.lower() == end.lower():
                continue
            else:
                flag = False
                break
        return flag

    def isPalindrome2(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome2(s))
