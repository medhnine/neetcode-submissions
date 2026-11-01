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

        
        # if len(nums) == k:
        #     return nums
        # unique = set(nums)
        # unique = list(unique)
        # i = 0 
        # result = {}
        # while True:
        #   if len(unique) == i:
        #     break
        #   count = 0
        # #   if len(nums) == 0:
        # #     break
        #   for n in nums:
        #     if
        #     if n == unique[i]:
        #       count += 1
        #   result[unique[i]] = count
        # #   nums = [x for x in nums if x != unique[i]]
        #   i += 1
        # x = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        # x = list(x)
        # return x[:k]

          
        # result = {}
        # if k == len(nums):
        #     return nums
        # for index, n in enumerate(nums):
        #     res1 = []
        #     if n in result:
        #         continue
        #     if index > 0:
        #         res1 = nums[:index-1]
        #     res2 = res1 + nums[index+1:]
        #     count = 1
        #     for x in res2:
        #         if n == x:
        #             count += 1
        #     result[n] = count
        # x = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        # x = list(x)
        # return x[:k]