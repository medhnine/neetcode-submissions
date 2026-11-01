class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        my_dic = {}
        for s in strs:
            elt = "".join(sorted(s))
            if elt not in my_dic:
                my_dic[elt] = [s]
            else:
                my_dic[elt].append(s)
        return list(my_dic.values())