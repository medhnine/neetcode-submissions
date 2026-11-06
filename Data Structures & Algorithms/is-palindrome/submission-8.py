class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        while start != end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start] == s[end]:
                end -= 1
                start += 1
                if start == int(len(s) / 2):
                  return True
            else:
                return False
        return True