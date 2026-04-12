class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash_table;

        int complement;
        for (int i = 0; i < nums.size(); i++) {
            complement = target - nums[i];

            if (hash_table.count(complement)) {
                return {hash_table[complement], i};
            } else {
                hash_table[nums[i]] = i;
            }
        }

        return {};
    }
};
