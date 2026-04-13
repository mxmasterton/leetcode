class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> hash_table_s, hash_table_t;

        for (int i = 0; i < s.length(); i++) {
            hash_table_s[s[i]] += 1;
            hash_table_t[t[i]] += 1;
        }

        return hash_table_s == hash_table_t;
    }
};
