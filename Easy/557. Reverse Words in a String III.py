class Solution:
    def reverseWords(self, s: str) -> str:
        answer = [''.join(reversed(i)) for i in s.split()]
        return ' '.join(answer)
