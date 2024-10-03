class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = []
        q = 0
        for i in nums:
            if i == 1:
                q += 1
            else:
                answer.append(q)
                q = 0
        else:
            answer.append(q)
        return max(answer)        