class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        lst = [2,3,5]

        for i in lst:
            while n % i == 0:
                n //= i   
        return n == 1