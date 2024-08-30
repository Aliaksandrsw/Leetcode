class Solution:
    def isValid(self, s: str) -> bool:
        q = {'}': '{', ')': '(', ']': '['}
        t = []

        for i in s:
            if i not in q:
                t.append(i)
            else:
                if not t or t[-1] != q[i]:
                    return False
                t.pop()

        return len(t) == 0
