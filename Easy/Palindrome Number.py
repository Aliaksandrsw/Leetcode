class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        x = str(x)
        return x == x[::-1]