class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) != magazine.count(i) and ransomNote.count(i) > magazine.count(i):
                return False

        else:
            return True
