class Solution:
    def max_subarray(self, nums: list[int]) -> int:

        current_max = 0
        final_max = nums[0]

        for num in nums:
            current_max = max ( num, current_max + num )
            final_max = max(current_max, final_max)