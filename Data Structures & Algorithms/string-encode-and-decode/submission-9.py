class Solution:
    def encode(self, strs):
        res = ""
        for index, x in enumerate(strs):
            res += "-->" + x
        return res
    def decode(self, s: str):
      res = s.split("-->")
      return res[1:]