class Solution:
    def isPalindrome(self, s) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

if __name__ == '__main__':
    s1 = Solution()
    print(s1.isPalindrome("A man, a plan, a canal: Panama"))