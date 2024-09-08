class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = [0]

        for i in range(len(gain)):
            s.append(gain[i]+ s[i])
        return max(s)