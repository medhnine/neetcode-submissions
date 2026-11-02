class Solution:
    def productExceptSelf(self, nums):
        p = 1
        result = [1] * len(nums)
        for index, n in enumerate(nums):
            result[index] = p
            p *= n
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result

        