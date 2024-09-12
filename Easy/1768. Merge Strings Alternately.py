class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            merge_lst = [i for q in zip(word1,word2) for i in q]
            return ''.join(merge_lst)
        elif len(word1) > len(word2):
            merge_lst = [i for q in zip(word1, word2) for i in q]
            for i in word1[len(word2):]:
                merge_lst.append(i)
            return ''.join(merge_lst)
        else:
            merge_lst = [i for q in zip(word1, word2) for i in q]
            for i in word2[len(word1):]:
                merge_lst.append(i)
            return ''.join(merge_lst)