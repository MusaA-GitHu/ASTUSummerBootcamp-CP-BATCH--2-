class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left  = 0
        right = len(nums) - 1
        max_s = 0

        while left < right:
            max_s = max(max_s, nums[left] + nums[right])
            left  += 1
            right -= 1

        return max_s
