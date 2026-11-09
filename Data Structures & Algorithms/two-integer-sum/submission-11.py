class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, n1 in enumerate(nums):
            for index2, n2 in enumerate(nums[index+ 1:]):
                if n1 + n2 == target:
                    return [index, index2 + index + 1]
        return res