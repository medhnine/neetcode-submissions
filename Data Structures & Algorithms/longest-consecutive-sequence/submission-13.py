class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        nums = set(nums)
        result = set()
        count = 0
        small = min(nums)
        while True:
            if small not in  nums:
                result.add(count)
                count = 0
                small = min(nums)
            nums.remove(small)
            count += 1
            small += 1
            if len(nums) == 0:
                result.add(count)
                return max(result)