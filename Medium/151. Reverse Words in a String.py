class Solution:
    def reverseWords(self, s: str) -> str:
        while '  ' in s:
            s = s.replace('  ', ' ')

        s = s.split()[::-1]
        s = ' '.join(s)
        return s
