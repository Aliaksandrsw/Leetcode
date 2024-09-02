class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = str(num ** 0.5)
        return (len(s[s.find('.')+1:]) <=1)      