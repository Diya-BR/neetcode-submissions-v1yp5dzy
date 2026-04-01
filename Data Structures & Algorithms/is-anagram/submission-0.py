class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
        if len(dict_s) == len(dict_t):
            for i in dict_s.keys():
                if i in dict_t:
                    if dict_s[i] != dict_t[i]:
                        return False
                else: 
                    return False
            return True
        return False


