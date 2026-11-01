class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #res = []

        if not strs:
            return []

        my_dic = {}

        for s in strs:

            # al_ha = [[0] * 26]

            # for c in s:

            #     al_ha[sorted(s)] += 1
            #     break
            elt = ""
            for c in sorted(s):
                elt += c
            
            if elt not in my_dic:

                my_dic[elt] = [s]
            else:
                my_dic[elt].append(s)
            
            # elt = tuple(al_ha)
            # if elt not in my_dic:
            #     my_dic[elt] = [s]
            # else:
            #     my_dic[elt].append(s)
        
        return list(my_dic.values())
        
