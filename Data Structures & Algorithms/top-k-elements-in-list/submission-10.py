class Solution:
    def topKFrequent(self, nums , k: int) :
        if len(nums) == k:
            return nums
        result = {}
        for n in nums:
          if n in result:
            result[n] += 1
          else:
            result[n] = 1
        x = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        x = list(x)
        return x[:k]