class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d_t = {}
        d_s = {}
        try:
            for i,v in enumerate(s):
                if v not in d_s:
                    d_s[v] = 1
                    d_t[t[i]] = 1
                else:
                    d_s[v] += 1
                    d_t[t[i]] += 1

                if list(d_s.values()) != list(d_t.values()):
                    return False
            else:
                return True
        except KeyError:
            return False