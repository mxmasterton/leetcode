class Solution:
    def isAnagram(self, string_s: str, string_t: str) -> bool:
        if len(string_s) != len(string_t):
            return False

        hash_s, hash_t = {}, {}

        for s, t in zip(string_s, string_t):
            hash_s[s] = hash_s.get(s, 0) + 1
            hash_t[t] = hash_t.get(t, 0) + 1

        return hash_s == hash_t
        