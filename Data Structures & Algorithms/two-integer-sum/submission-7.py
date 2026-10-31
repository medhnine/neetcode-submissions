class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            value = target - nums[i]
            temp = nums[i + 1:]
            if value in temp:
                index = temp.index(value) + 1 +  i
                return [i, index]
            i += 1
