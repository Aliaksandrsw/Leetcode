class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        m_dict = {}  
        max_len = 0  
        start = 0  

        for i in range(len(s)):
            if s[i] in m_dict and m_dict[s[i]] >= start:
                start = m_dict[s[i]] + 1
            m_dict[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len

