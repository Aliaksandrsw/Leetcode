class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_d = {}

        for i,v in enumerate(numbers):
            my_sum = target - v
            if my_sum in my_d:
                return [my_d[my_sum] + 1, i + 1]
            my_d[v] = i