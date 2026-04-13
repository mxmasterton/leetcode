class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}

        for i in range(len(s)):
            if s[i] in hash_map_s:
                hash_map_s[s[i]] += 1
            else:
                hash_map_s[s[i]] = 1

            if t[i] in hash_map_t:
                hash_map_t[t[i]] += 1
            else:
                hash_map_t[t[i]] = 1

        return hash_map_s == hash_map_t
        