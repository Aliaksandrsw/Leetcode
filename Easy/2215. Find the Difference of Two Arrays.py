class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        q = set(nums1) - set(nums2)
        q_1 = set(nums2) - set(nums1)
        return [list(q), list(q_1)]