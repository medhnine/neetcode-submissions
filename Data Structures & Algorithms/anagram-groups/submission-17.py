class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res = {}
        for s in strs:
            store = "".join(sorted(s))
            if store not in res:
                res[store] = [s]
            else:
                res[store].append(s)
        return list(res.values())