
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        left = 1
        right = 1

        for i in range(1, len(nums)):
            left *= nums[i-1]
            res[i] *= left

        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        return res

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
# output: [24, 12, 8, 6]
