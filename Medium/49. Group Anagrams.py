class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))

            if sorted_str not in dict_anagram:
                dict_anagram[sorted_str] = []
            dict_anagram[sorted_str].append(i)

        return list(dict_anagram.values())
