class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()[-1]
        return len(s)