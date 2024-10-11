class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        for i in range(0, len(s), 2*k):
            result.extend(reversed(s[i:i + k]))
            result.extend(s[i + k:i + 2*k])
        return ''.join(result)
