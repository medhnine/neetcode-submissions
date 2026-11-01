class Solution:
    def encode(self, strs):
        res = ""
        for x in strs:
            res += "-->" + x
        return res
    def decode(self, s: str):
      res = s.split("-->")
      return res[1:]
