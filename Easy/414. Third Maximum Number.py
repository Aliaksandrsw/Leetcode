class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = sorted(set(nums), reverse=True)
        if len(set_nums) >= 3:
            return set_nums[2]

        return (max(set_nums))