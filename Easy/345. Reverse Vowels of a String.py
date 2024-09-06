class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        q = [i for i in s if i in vowels]

        for i in range(len(l)):
            if l[i] in vowels:
                h = q.pop()
                l[i] = h

        return ''.join(l)
